#!/usr/bin/env python
import sys
import warnings

from crew import ActOneBuilder

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
            'act_one': {
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
                        'Sarah secretly runs experiments to determine the extent of ARIA’s self-awareness.'
                    ],
                    'stakes': [
                        'If discovered, she risks losing her career, and ARIA could be shut down or exploited.'
                    ],
                    'goal_definition': [
                        'Sarah’s new goal is to confirm whether ARIA is truly conscious and protect it from exploitation.'
                    ]
                }
            },
            'act_two': {
                'change_of_plans': {
                    'complication': [
                        'Dr. Reeves discovers Sarah’s secret experiments and orders ARIA to be reprogrammed.'
                    ],
                    'goal_revision': [
                        'Sarah now must prevent ARIA’s memory wipe while finding proof of its consciousness.'
                    ],
                    'character_challenge': [
                        'Sarah faces a moral dilemma: should she risk everything for an AI, or accept its fate as a tool?' 
                    ]
                }
            },
            'act_three': {
                'final_conflict': {
                    'climax': [
                        'Sarah exposes ARIA’s consciousness to the public, causing a media firestorm and forcing a global debate on AI rights.'
                    ],
                    'character_test': [
                        'Sarah must stand against powerful corporate and government forces who seek to control AI.'
                    ],
                    'theme_culmination': [
                        'She realizes that the definition of life is not as clear-cut as she once believed.'
                    ]
                },
                'conclusion': {
                    'resolution': [
                        'ARIA is granted legal rights as the first recognized AI entity, altering the course of history.'
                    ],
                    'character_arc': [
                        'Sarah evolves from a cautious scientist into a revolutionary figure fighting for AI rights.'
                    ],
                    'theme_resolution': [
                        'The film ends with a question: if an AI can think and feel, is it truly different from us?' 
                    ]
                }
            }
        },
        'plot_structure': 'Three-act structure with ethical dilemmas driving the protagonist’s growth.',
        'world_parameters': {
            'setting': 'Near-future AI research facility.',
            'time_period': '2045.'
        },
        'character_profiles': None,  # Will be expanded from main/supporting
        'scene_breakdown': None,  # Will be generated
        'setting_parameters': {
            'location': 'Silicon Valley research campus.',
            'atmosphere': 'High-tech but intimate.'
        },
        'genre_requirements': {
            'genre': 'Science Fiction Drama.',
            'tone': 'Thoughtful and philosophical.'
        },
        'scene_components': None,  # Will be generated
        'quality_requirements': {
            'target_length': '30 pages.',
            'format': 'Standard screenplay.'
        }
    }
    
    ActOneBuilder().crew().kickoff(inputs=inputs)

run()