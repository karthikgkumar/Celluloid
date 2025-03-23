# app.py
from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel, field_validator
from typing import Optional, Dict, List, Any
from logline_agent import LoglineTool
from central_message import CentralMessageTool

import os
from dotenv import load_dotenv
load_dotenv()

from character_builder.crew import CharacterBuilder
import json

from fastapi.middleware.cors import CORSMiddleware

apiKey = os.getenv('SECURE')
API_KEY_NAME ='X-API-Key'
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != apiKey:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key


app = FastAPI(
    title="Logline Generator API",
    description="API for generating movie loglines from abstracts",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
async def generate_logline(request: LoglineRequest,api_key : str = Depends(verify_api_key) ):
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
    
######CENTRAL MESSAGE AGENT##############
######INPUT###############
# {
#     "logline": "In a high-stakes battle for power...",
#     "story_elements": {
#         "main_character": "Stephen Nedumpally...",
#         "primary_mission": "To navigate the treacherous political landscape...",
#         "up_against": "Stephen faces internal factions...",
#         "at_stake": "Stephen's loyalty, principles..."
#     }
# }
central_message_tool=CentralMessageTool()

class StoryElements(BaseModel):
    main_character: str
    primary_mission: str
    up_against: str
    at_stake: str

class CentralMessageRequest(BaseModel):
    logline: str
    story_elements: StoryElements

class CentralMessageResponse(BaseModel):
    protagonist_belief: str
    antagonist_belief: str
    central_message: str

@app.post("/central-message/", response_model=CentralMessageResponse)
async def generate_central_message(request: CentralMessageRequest,api_key : str = Depends(verify_api_key)):
    try:
        # Convert story elements to dictionary format
        story_elements_dict = {
            "main_character": request.story_elements.main_character,
            "primary_mission": request.story_elements.primary_mission,
            "up_against": request.story_elements.up_against,
            "at_stake": request.story_elements.at_stake
        }
        
        # Generate central message using the provided logline and story elements
        result = central_message_tool._run(
            logline=request.logline,
            story_elements=story_elements_dict
        )
        
        if isinstance(result, str) and "Error" in result:
            raise HTTPException(status_code=400, detail=result)
            
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


character_builder = CharacterBuilder()
class CharacterRequest(BaseModel):
    abstract: str
    logline: Optional[str] = None
    central_message: Optional[str] = None
    character_details: Optional[str] = None

    @field_validator('abstract', 'logline', 'central_message', 'character_details', mode="before")
    @classmethod
    def clean_text(cls, v):
        if v:
            return ' '.join(line.strip() for line in v.splitlines() if line.strip())
        return v

class CharacterResponse(BaseModel):
    abstract: str
    logline: Optional[str] = None
    central_message: Optional[str] = None
    genre : Optional[str] = None
    main_characters: List[Dict[str, Any]]  # A list of character dictionaries
    supporting_characters: List[Dict[str, Any]]  # A list of character dictionaries

@app.post("/character-agent/", response_model=CharacterResponse)
async def generate_character(request: CharacterRequest,api_key : str = Depends(verify_api_key)):
    try:
        inputs = {
            "abstract": request.abstract,
            "logline": request.logline,
            "central_message": request.central_message,
            "character_details": request.character_details
        }

        # Run the character agent
        crew_result = character_builder.crew().kickoff(inputs=inputs)

        # Debugging output
        print("Type of result:", type(crew_result))
        
        # Extract the raw JSON from the CrewOutput object
        if hasattr(crew_result, 'raw'):
            raw_result = crew_result.raw
            # If raw_result starts with ```json and ends with ```, strip those markers
            if isinstance(raw_result, str) and raw_result.startswith('```json') and raw_result.endswith('```'):
                raw_result = raw_result[7:-3].strip()
            
            try:
                # Parse the JSON string
                parsed_result = json.loads(raw_result)

                # Construct the response
                response = {
                    "abstract": request.abstract,
                    "logline": request.logline,
                    "central_message": request.central_message,
                    "genre": None,
                    "main_characters": parsed_result.get("main_characters", []),
                    "supporting_characters": parsed_result.get("supporting_characters", [])
                }
                
                # Validate the parsed result against CharacterResponse
                return CharacterResponse(**response)
            except json.JSONDecodeError as e:
                print("JSON Decode Error:", e)
                raise HTTPException(status_code=500, detail=f"Error parsing JSON from CharacterBuilder: {e}")
        else:
            print("Result does not have 'raw' attribute:", crew_result)
            raise HTTPException(status_code=500, detail="Unexpected response structure from CharacterBuilder")

    except Exception as e:
        print("Error in API:", e)
        raise HTTPException(status_code=500, detail=str(e))


###########OUTPUT##############
# {
#     "protagonist_belief": "protagonist's belief statement",
#     "antagonist_belief": "antagonist's belief statement",
#     "central_message": "synthesized central message"
# }
@app.get("/")
async def root():
    return {"message": "Welcome to Logline Generator API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)

#response
# {
#   "logline": "In a high-stakes battle for power and righteousness within the ruling party, loyal Stephen Nedumpally must confront betrayals, navigate treachery, and face off against the corrupt son-in-law to safeguard his principles and the party's future.",
#   "story_elements": {
#     "main_character": "Stephen Nedumpally, a loyal party member with a mysterious past who becomes a pivotal figure in the chaotic power struggle within the ruling party.",
#     "primary_mission": "To navigate the treacherous political landscape, uphold his principles, and emerge victorious in the battle for dominance within the party.",
#     "up_against": "Stephen faces internal factions within the ruling party vying for power, particularly Bobby, the late leader's corrupt son-in-law who seeks personal gain and poses a significant threat.",
#     "at_stake": "Stephen's loyalty, principles, and the future of the party are at stake as he navigates a web of secrets, betrayals, and conspiracies in a high-stakes fight against corruption and for righteousness."
#   }
# }
# In this JSON:

# The string is enclosed in double quotes.
# Newlines are represented by \n\n to separate paragraphs.
# Single quotes (like in "state's" or "there's") remain unchanged, as they are valid within a double-quoted JSON string.


