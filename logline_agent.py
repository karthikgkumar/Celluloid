import openai
import os
from typing import Dict, Optional

class LoglineTool:
    def __init__(self):
        self.system_prompt = """
        You are an expert screenwriter and story consultant specializing in creating compelling loglines. 
        Your task is to analyze movie abstracts and generate engaging, concise loglines that capture the 
        essence of the story in a single sentence. Focus on the protagonist, conflict, stakes, and hook.
        """

    def _run(self, abstract: str, genre: Optional[str] = None) -> Dict:
        try:
            # Generate story elements
            story_elements = self._generate_story_elements(abstract, genre)
            
            # Generate final logline
            logline = self._generate_logline(story_elements)
            
            return {
                "logline": logline,
                "story_elements": story_elements
            }
        except Exception as e:
            return f"Error: {e}"

    def _generate_story_elements(self, abstract: str, genre: Optional[str]) -> Dict:
        prompt = f"""
        Analyze this movie abstract and generate the key story elements:
        Abstract: {abstract}
        Genre: {genre if genre else 'Not specified'}

        Provide the following elements in a Python dictionary format:
        1. main_character: Detailed description of the protagonist
        2. primary_mission: The main goal/mission of the protagonist
        3. up_against: Main obstacles and antagonists
        4. at_stake: What the character stands to lose

        Format as a Python dictionary with these exact keys.
        """

        response = self._get_openai_response(prompt)
        return self._parse_response(response)

    def _generate_logline(self, story_elements: Dict) -> str:
        prompt = f"""
        Using these story elements, create a compelling one-sentence logline:
        
        Main Character: {story_elements['main_character']}
        Primary Mission: {story_elements['primary_mission']}
        Up Against: {story_elements['up_against']}
        At Stake: {story_elements['at_stake']}

        The logline should:
        - Be exactly one sentence
        - Include the protagonist's key characteristic
        - State the main conflict
        - Hint at the stakes
        - Create an emotional hook
        - Be under 50 words

        Return only the logline with no additional text.
        """

        response = self._get_openai_response(prompt)
        return response.strip()

    def _get_openai_response(self, prompt: str) -> str:
        try:
            openaiclient = openai.Client(
                api_key=os.getenv('OPENAI_API_KEY'),
                base_url=os.getenv('OPENAI_BASE_URL')
            )

            msg = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt},
            ]

            response = openaiclient.chat.completions.create(
                messages=msg,
                temperature=0.7,
                model=os.getenv('OPENAI_MODEL'),
                max_tokens=500,
                stream=False,
            )
            
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating content: {e}"

    def _parse_response(self, response: str) -> Dict:
        try:
            # Find the dictionary in the response and evaluate it
            dict_start = response.find('{')
            dict_end = response.rfind('}') + 1
            
            if dict_start == -1 or dict_end == -1:
                raise ValueError("No dictionary found in response")
            
            dict_str = response[dict_start:dict_end]
            return eval(dict_str)
        except Exception as e:
            # Fallback dictionary if parsing fails
            return {
                "main_character": "Error parsing character description",
                "primary_mission": "Error parsing mission",
                "up_against": "Error parsing obstacles",
                "at_stake": "Error parsing stakes"
            }