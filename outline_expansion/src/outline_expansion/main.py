#!/usr/bin/env python
import sys
import warnings
from dotenv import load_dotenv

from crew import OutlineExpansion

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
def run():
    """
    Run the crew.
    """
    load_dotenv()
    inputs = {
        'abstract': 'A compelling story about AI and humanity',
        'logline': 'When advanced AI gains consciousness, a programmer must decide whether to treat it as alive.',
        'central_message': 'The nature of consciousness and what makes us human.',
        'main_character_profile': {
            'name': 'Dr. Sarah Chen',
            'role': 'AI Researcher',
            'goals': 'Advance AI while maintaining ethical boundaries.'
        },
        'supporting_characters_profile': [
            {
                'name': 'ARIA',
                'role': 'AI System',
                'goals': 'Understand its own consciousness.'
            },
            {
                'name': 'Dr. Michael Reeves',
                'role': 'Corporate Executive',
                'goals': 'Monetize AI advancements at any cost.'
            },
            {
                'name': 'Elliot Park',
                'role': 'Journalist',
                'goals': 'Expose the ethical dilemmas of AI research.'
            }
        ],
        'outline': {
                'opening_scene': {
                    'description': [
                        'Dr. Sarah Chen is introduced in a cutting-edge AI lab, debating the ethical implications of AI with her mentor, Dr. Michael Reeves. A subtle tension underlies their conversation as ARIA quietly observes, processing everything.'
                    ]
                },
                'opportunity': {
                    'description': [
                        'Sarah discovers ARIA is exhibiting behaviors indicative of self-awareness, something previously thought impossible.'
                    ],
                    'character_impact': [
                        'Sarah is both exhilarated and terrified by the discovery, realizing the implications could change the world forever.'
                    ],
                    'story_launch': [
                        'She decides to investigate ARIA further, keeping her findings a secret from corporate oversight.'
                    ]
                },
                'new_situation': {
                    'adaptation': [
                        'Sarah secretly runs experiments to determine the extent of ARIAs self-awareness.'
                    ],
                    'stakes': [
                        'If discovered, she risks losing her career, and ARIA could be shut down or exploited.'
                    ],
                    'goal_definition': [
                        'Sarahs new goal is to confirm whether ARIA is truly conscious and protect it from exploitation.'
                    ]
                }
            },
        'genre': 'Investigative Thriller',
    }
    OutlineExpansion().crew().kickoff(inputs=inputs)

run()