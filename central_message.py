from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from typing import Dict, Optional
import os
from dotenv import load_dotenv
load_dotenv()

class CentralMessageTool:
    def __init__(self):
        self.system_prompt = """
        You are an expert story consultant and narrative analyst specializing in understanding 
        character beliefs and thematic messages. Your task is to analyze story elements and 
        generate profound character beliefs and central messages that form the philosophical 
        core of the story.
        """
        self.llm = ChatOpenAI(
            model_name=os.getenv('OPENAI_MODEL'),
            temperature=0.7,
            api_key=os.getenv('OPENAI_API_KEY')
        )

    def _run(self, logline: str, story_elements: Dict) -> Dict:
        try:
            # Generate protagonist belief
            protagonist_belief = self._generate_protagonist_belief(logline, story_elements)
            
            # Generate antagonist belief
            antagonist_belief = self._generate_antagonist_belief(logline, story_elements, protagonist_belief)
            
            # Generate central message
            central_message = self._generate_central_message(protagonist_belief, antagonist_belief)
            
            return {
                "protagonist_belief": protagonist_belief,
                "antagonist_belief": antagonist_belief,
                "central_message": central_message
            }
        except Exception as e:
            return f"Error: {e}"

    def _generate_protagonist_belief(self, logline: str, story_elements: Dict) -> str:
        prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=f"""
                Analyze these story elements and generate the protagonist's deeply held belief:
                
                Logline: {logline}
                Main Character: {story_elements['main_character']}
                Primary Mission: {story_elements['primary_mission']}
                Up Against: {story_elements['up_against']}
                At Stake: {story_elements['at_stake']}

                Generate a single-sentence belief that:
                - Represents the protagonist's worldview at the start
                - Is flawed or incomplete
                - Is demonstrated through their actions
                - Will be challenged throughout the story

                Return only the belief statement with no additional text.
            """)
        ])

        response = self.llm.invoke(prompt.format_messages())
        return response.content.strip()

    def _generate_antagonist_belief(self, logline: str, story_elements: Dict, protagonist_belief: str) -> str:
        prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=f"""
                Analyze these elements and generate the antagonist's opposing belief:
                
                Logline: {logline}
                Up Against: {story_elements['up_against']}
                Protagonist's Belief: {protagonist_belief}

                Generate a single-sentence belief that:
                - Is the direct opposite of the protagonist's belief
                - Represents the antagonist's worldview
                - Remains consistent throughout the story
                - Creates meaningful philosophical conflict

                Return only the belief statement with no additional text.
            """)
        ])

        response = self.llm.invoke(prompt.format_messages())
        return response.content.strip()

    def _generate_central_message(self, protagonist_belief: str, antagonist_belief: str) -> str:
        prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=f"""
                Using these opposing beliefs, create a central message that synthesizes them:
                
                Protagonist's Initial Belief: {protagonist_belief}
                Antagonist's Belief: {antagonist_belief}

                Generate a single-sentence message that:
                - Combines elements of both beliefs
                - Represents a higher truth
                - Shows the protagonist's growth
                - Delivers the story's ultimate wisdom

                Return only the central message with no additional text.
            """)
        ])

        response = self.llm.invoke(prompt.format_messages())
        return response.content.strip()
    
#####Input##########
# curl -X 'POST' \
#   'http://127.0.0.1:8000/central-message/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "logline": "A guilt-ridden dream thief must plant an idea instead of stealing one, facing his inner demons and the threat of eternal dream entrapment in a mind-bending race against time.",
#   "story_elements": {
#     "main_character": "Dom Cobb, a skilled thief haunted by his past and seeking redemption, who excels in extracting secrets from deep within the subconscious by infiltrating dreams.",
#     "primary_mission": "To plant an idea in someone'\''s mind instead of stealing one, which is considered an impossible task.",
#     "up_against": "Cobb is up against the challenge of navigating multiple layers of dreams within dreams, his own inner demons, and the blurring line between reality and the dream world.",
#     "at_stake": "Cobb risks being trapped in a dream forever if he fails to successfully complete the mission within a time limit while facing danger at every level."
#   }
# }'
####output####
# {
#   "protagonist_belief": "\"I can only find redemption by delving deeper into the subconscious and manipulating dreams to escape my guilt.\"",
#   "antagonist_belief": "\"True redemption comes from accepting and embracing one's guilt, not by manipulating dreams to escape it.\"",
#   "central_message": "True redemption lies not in escaping guilt through manipulation, but in facing it with courage and acceptance within the depths of our own subconscious."
# }