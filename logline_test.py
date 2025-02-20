# test_logline.py
import os
from dotenv import load_dotenv
from logline_agent import LoglineTool  # Assuming the above code is saved in logline_tool.py

# Load environment variables from .env file
load_dotenv()

def test_logline_generator():
    # Create an instance of LoglineTool
    tool = LoglineTool()
    
    # Test case 1: A sample movie abstract
    test_abstract = """
    In a dystopian future, a skilled hacker discovers a way to access people's memories. 
    When she stumbles upon a conspiracy involving the government manipulating citizens' 
    memories, she must decide whether to expose the truth while protecting her family 
    from those who want to keep the secret buried.
    """
    
    # Test with genre
    result = tool._run(
        abstract=test_abstract,
        genre="Science Fiction"
    )
    
    # Print results
    print("\nTest Case 1 (with genre):")
    print("Logline:", result["logline"])
    print("\nStory Elements:")
    for key, value in result["story_elements"].items():
        print(f"{key}: {value}")

    # Test case 2: Another example without genre
    test_abstract_2 = """
    A retired chef who lost his sense of taste must return to the culinary world 
    to save his daughter's failing restaurant. While rediscovering his passion 
    for cooking, he struggles with his disability and his strained relationship 
    with his daughter.
    """
    
    result_2 = tool._run(
        abstract=test_abstract_2
    )
    
    print("\nTest Case 2 (without genre):")
    print("Logline:", result_2["logline"])
    print("\nStory Elements:")
    for key, value in result_2["story_elements"].items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    test_logline_generator()