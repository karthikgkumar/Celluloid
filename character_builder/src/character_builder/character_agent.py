from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from typing import Optional, Dict, List, Any
import json
from character_builder.crew import CharacterBuilder

app = FastAPI(
    title="Character Agent API",
    description="API for generating character details from an abstract",
    version="1.0.0"
)

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
    genre: Optional[str] = None
    characters: List[Dict[str, Any]]  # A list of character dictionaries

@app.post("/character-agent/", response_model=CharacterResponse)
async def generate_character(request: CharacterRequest):
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
                
                # Validate the parsed result against CharacterResponse
                return CharacterResponse(**parsed_result)
            except json.JSONDecodeError as e:
                print("JSON Decode Error:", e)
                raise HTTPException(status_code=500, detail=f"Error parsing JSON from CharacterBuilder: {e}")
        else:
            print("Result does not have 'raw' attribute:", crew_result)
            raise HTTPException(status_code=500, detail="Unexpected response structure from CharacterBuilder")

    except Exception as e:
        print("Error in API:", e)
        raise HTTPException(status_code=500, detail=str(e))