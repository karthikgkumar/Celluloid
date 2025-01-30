import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field, validator
from typing import Optional, Dict
import openai
from logline_agent import LoglineTool
from dotenv import load_dotenv
import json
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Logline Generator API",
    description="API for generating movie loglines from abstracts",
    version="1.0.0"
)

class LoglineRequest(BaseModel):
    abstract: str = Field(
        description="The movie abstract/summary from which to generate a logline"
    )
    genre: Optional[str] = Field(
        default=None,
        description="Optional genre of the movie"
    )

    @validator('abstract')
    def clean_abstract(cls, v):
        # Remove null bytes and other control characters
        v = ''.join(char for char in v if ord(char) >= 32 or char in '\n\r\t')
        return v.strip()

    @validator('genre')
    def clean_genre(cls, v):
        if v:
            # Remove control characters from genre
            v = ''.join(char for char in v if ord(char) >= 32 or char in '\n\r\t')
            return v.strip()
        return v

class LoglineResponse(BaseModel):
    logline: str = Field(description="Generated one-sentence logline")
    story_elements: Dict = Field(description="Detailed story elements used to generate the logline")

sys_prompt = """
You are a professional screenwriter assistant specialized in creating compelling loglines 
for movie scripts. You analyze movie abstracts and generate concise, engaging loglines 
that capture the essence of the story. You focus on the protagonist, conflict, stakes, 
and emotional hook while keeping the logline to a single sentence.
"""

tools = [
    {
        "type": "function",
        "function": {
            "name": "generate_logline",
            "description": "Generates a logline and story elements from a movie abstract",
            "parameters": {
                "type": "object",
                "properties": {
                    "abstract": {
                        "type": "string",
                        "description": "The movie abstract/summary"
                    },
                    "genre": {
                        "type": "string",
                        "description": "Optional genre of the movie"
                    }
                },
                "required": ["abstract"]
            }
        }
    }
]

def sanitize_json_string(s: str) -> str:
    """Sanitize a string for JSON encoding"""
    if not s:
        return s
    # Replace problematic characters
    replacements = {
        '\n': '\\n',
        '\r': '\\r',
        '\t': '\\t',
        '"': '\\"'
    }
    for old, new in replacements.items():
        s = s.replace(old, new)
    return s

@app.post("/logline-agent", response_model=LoglineResponse)
async def create_logline(request: LoglineRequest):
    try:
        logger.debug("Starting logline generation process")
        logger.debug(f"Input abstract: {request.abstract[:100]}...")
        logger.debug(f"Input genre: {request.genre}")

        # Initialize OpenAI client
        openaiclient = openai.Client(
            api_key=os.getenv('OPENAI_API_KEY'),
            base_url=os.getenv('OPENAI_BASE_URL')
        )
        logger.debug("OpenAI client initialized")

        # Sanitize the input
        sanitized_abstract = sanitize_json_string(request.abstract)
        sanitized_genre = sanitize_json_string(request.genre) if request.genre else None
        logger.debug("Input sanitization completed")

        # Initial messages
        messages = [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": f"Generate a logline for this movie abstract:\n\n{sanitized_abstract}" + 
             (f"\nGenre: {sanitized_genre}" if sanitized_genre else "")}
        ]
        logger.debug("Messages prepared for OpenAI")

        # Get OpenAI's response
        logger.debug(f"Making OpenAI API call with model: {os.getenv('OPENAI_MODEL')}")
        response = openaiclient.chat.completions.create(
            model=os.getenv('OPENAI_MODEL'),
            messages=messages,
            tools=tools,
            max_tokens=1000
        )
        logger.debug("Received response from OpenAI")

        # Process the response
        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls
        logger.debug(f"Number of tool calls received: {len(tool_calls) if tool_calls else 0}")
        
        if tool_calls:
            tool_call = tool_calls[0]
            try:
                logger.debug(f"Raw function arguments: {tool_call.function.arguments}")
                function_args = json.loads(tool_call.function.arguments)
                logger.debug("Successfully parsed function arguments")
            except json.JSONDecodeError as e:
                logger.error(f"JSON parsing failed: {str(e)}")
                # If JSON parsing fails, try to clean the string and parse again
                cleaned_args = sanitize_json_string(tool_call.function.arguments)
                logger.debug(f"Attempting with cleaned arguments: {cleaned_args}")
                function_args = json.loads(cleaned_args)
            
            # Use LoglineTool to generate the logline
            logger.debug("Initializing LoglineTool")
            logline_tool = LoglineTool()
            result = logline_tool._run(
                abstract=function_args['abstract'],
                genre=function_args.get('genre')
            )
            logger.debug("LoglineTool execution completed")
            
            return LoglineResponse(
                logline=result["logline"],
                story_elements=result["story_elements"]
            )
        else:
            logger.error("No tool calls were generated in the response")
            raise HTTPException(status_code=500, detail="No tool calls generated")
            
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {str(e)}")
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid JSON format in request or response: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500, 
            detail=f"An error occurred: {str(e)}"
        )



@app.get("/", response_class=RedirectResponse)
def redirect_to_docs():
    return "/docs"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)