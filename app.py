# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from typing import Optional
from logline_agent import LoglineTool

app = FastAPI(
    title="Logline Generator API",
    description="API for generating movie loglines from abstracts",
    version="1.0.0"
)
# abstract=""""The movie revolves around the intense political drama that unfolds following the death of a state's Chief Minister. The story explores the chaotic power struggle within the ruling party, where various factions with their own agendas battle for dominance. Central to the narrative is a character named Stephen Nedumpally, a loyal party member with a mysterious past, who emerges as a pivotal figure in the conflict.\n\nOn the other side, there's Bobby, the late leader's son-in-law, who harbors corrupt intentions and seeks to exploit the situation for personal gain. As the power struggle intensifies, secrets, betrayals, and conspiracies come to light, creating a gripping tale of politics, loyalty, and the fight against corruption. The film delves into themes of morality, power, and the price of righteousness, all while delivering high-octane action and emotional depth.\n\nThis concept sets the stage for a compelling political action thriller with plenty of twists, dramatic character arcs, and a climactic reveal of the protagonist's true motives. It could also lay the foundation for sequels, exploring the protagonist's backstory and the consequences of the events in the first installment."

# Initialize the LoglineTool
logline_tool = LoglineTool()

class LoglineRequest(BaseModel):
    abstract: str
    genre: Optional[str] = None

    @field_validator('abstract')
    @classmethod
    def clean_abstract(cls, v):
        # Remove '#' markers and clean up newlines
        v = v.replace('#', '')
        # Normalize newlines and remove excessive whitespace
        lines = [line.strip() for line in v.splitlines()]
        return ' '.join(line for line in lines if line)

class LoglineResponse(BaseModel):
    logline: str
    story_elements: dict

@app.post("/logline-agent/", response_model=LoglineResponse)
async def generate_logline(request: LoglineRequest):
    try:
        result = logline_tool._run(
            abstract=request.abstract,
            genre=request.genre
        )
        
        if isinstance(result, str) and "Error" in result:
            raise HTTPException(status_code=400, detail=result)
            
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to Logline Generator API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)