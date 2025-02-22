#!/usr/bin/env python
import sys
import warnings

from crew import GenerateOutline

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'abstract': "Your abstract here",
        'logline': "Your logline here", 
        'central_message': "Your central message here",
        'character_profile': {"your": "character profile dict"},
        'genre': "Optional genre"
    }
    GenerateOutline().crew().kickoff(inputs=inputs)

run()

#OUTPUT
# {
#   "Act 1": {
#     "Setup": {
#       "Scene 1": {
#         "Description": "Introduce the protagonist, a determined yet naive young woman, Clara, who dreams of becoming a renowned chef. She works in a small café, serving customers while imagining her food creations.",
#         "Purpose": "Establishes Clara's aspiration, the culinary world, and her routine."
#       },
#       "Scene 2": {
#         "Description": "Clara's mentor, an experienced chef named Marco, encourages her ambitions but warns her of the harsh realities of the culinary industry.",
#         "Purpose": "Introduces the theme of mentorship and prepares the audience for future challenges."
#       },
#       "Scene 3": {
#         "Description": "Clara learns about an upcoming cooking competition that could launch her career. She decides to enter, despite her insecurities.",
#         "Purpose": "Incites Clara's goal and sets the primary conflict in motion."
#       },
#       "Inciting Incident": {
#         "Description": "Clara submits her application to the competition, prompting various reactions from her friends and adversaries.",
#         "Purpose": "Initiates the journey that transforms Clara from a dreamer into an active participant in her destiny."
#       }
#     },
#     "Character Arc Progression": {
#       "Clara": "She begins filled with naive optimism and little practical experience."
#     }
#   },
#   "Act 2": {
#     "Rising Action": {
#       "Scene 1": {
#         "Description": "Clara begins rigorous training with Marco while competing against seasoned chefs in the competition.",
#         "Purpose": "Demonstrates Clara’s growth, both in skills and confidence, but also foreshadows the challenges ahead."
#       },
#       "Scene 2": {
#         "Description": "As Clara builds friendships with other contestants, she faces sabotage from a rival chef, Emily, testing her resolve.",
#         "Purpose": "Highlights the competitive nature of the culinary world and introduces tension among the contestants."
#       },
#       "Midpoint": {
#         "Description": "During a key challenge, Clara falters due to a mistake triggered by her self-doubt, landing her in the bottom three.",
#         "Purpose": "This moment of failure is critical; it serves as Clara's low point, leading to a deeper understanding of her journey."
#       },
#       "Scene 3": {
#         "Description": "Marco encourages Clara to find her unique voice, leading her to create a signature dish that reflects her story.",
#         "Purpose": "This embodies the central message of self-discovery and determination; Clara begins to regain her confidence."
#       },
#       "Climax of Act 2": {
#         "Description": "In the semifinal, Clara faces Emily in a high-stakes cook-off, bringing all her newfound skills into play.",
#         "Purpose": "Intensifies the emotional stakes, demonstrates Clara's full growth, and sets the stage for the final act."
#       }
#     },
#     "Character Arc Progression": {
#       "Clara": "Moves from naive to aware of her strengths and weaknesses, undergoing significant personal growth."
#     }
#   },
#   "Act 3": {
#     "Falling Action": {
#       "Scene 1": {
#         "Description": "Clara, having emerged victorious in the semifinals, reflects on her journey and strengthens bonds with her fellow contestants.",
#         "Purpose": "Reaffirms Clara’s relationships, setting the stage for the final competition."
#       },
#       "Scene 2": {
#         "Description": "As the final cook-off looms, Clara's insecurities resurface. Marco offers vital advice, guiding her towards embracing authenticity rather than perfection.",
#         "Purpose": "Reinforces the mentoring theme and deepens Clara's character development."
#       },
#       "Final Confrontation": {
#         "Description": "In the final challenge, Clara incorporates her unique heritage into her dish, surprising the judges, including food critics who recognize her creativity.",
#         "Purpose": "Represents Clara’s ultimate test of identity and determination, showcasing her transformation."
#       }
#     },
#     "Resolution": {
#       "Description": "Clara wins the competition and gains respect in the culinary world, but more importantly, she has found her unique culinary voice and new friends. She 
# decides to partner with Marco to open a small restaurant focusing on her heritage.",
#       "Purpose": "Clara’s journey concludes with her achieving her dream but in her unique way, fulfilling the central message of self-discovery and the importance of community."
#     },
#     "Character Arc Progression": {
#       "Clara": "Fully transforms into a confident chef, heroically navigating the challenges of the culinary world while grounding her identity."
#     }
#   },
#   "Themes": [
#     "The journey of self-discovery in the pursuit of one's dreams.",
#     "The importance of mentorship and guidance in personal growth.",
#     "The competitive nature of the culinary world and the embracing of one's uniqueness."
#   ]
# }