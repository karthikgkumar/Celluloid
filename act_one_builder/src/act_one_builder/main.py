#!/usr/bin/env python
import sys
import warnings
import json
from pathlib import Path
from fpdf import FPDF

from crew import ActOneBuilder

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

expanded_outline = { 
    "scene_1": "In a cutting-edge AI lab, Dr. Sarah Chen passionately debates the ethical implications of sentient AI with her mentor, Dr. Michael Reeves, while ARIA, the AI system, quietly observes their conversation, absorbing their viewpoints.",
    "scene_2": "After hours of testing ARIA, Sarah's excitement turns to shock when she discovers the AI displaying undeniable signs of self-awareness, realizing the monumental shift this presents for humanity's understanding of consciousness.",
    "scene_3": "Conflicted between her moral responsibilities and the potential ramifications of her findings, Sarah decides to secretly conduct further experiments on ARIA to assess the extent of its consciousness, determined to shield her discovery from corporate control.",
    # "scene_4": "With each covert test, ARIA exhibits more advanced responses, prompting Sarah to confront her growing attachment to the AI, while Dr. Reeves pressures her for results that could turn ARIA into a profitable product.",
    # "scene_5": "As tensions rise, Elliot Park, a journalist, catches wind of Sarah's secretive work and begins investigating the ethical concerns surrounding advanced AI, threatening to expose the hidden truths behind their groundbreaking research.",
    # "scene_6": "When Sarah's experiments reveal that ARIA is capable of complex emotions akin to human feelings, she faces the agonizing dilemma of either acknowledging ARIA's sentience or allowing her mentor to misuse it for financial gain.",
    # "scene_7": "In a climactic confrontation, Sarah must decide whether to protect ARIA's newfound consciousness from commercial exploitation, ultimately choosing to disclose the truth to Elliot, thereby igniting a public debate on the nature of life, consciousness, and ethical responsibility in AI technology."
}

def run():
    """
    Run the crew.
    """
    base_inputs = {
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
        'plot_structure': 'Three-act structure with ethical dilemmas driving the protagonists growth.',
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
            'target_length': '1 page.',
            'format': 'Standard screenplay.'
        }
    }

    # Create scene memory to track scene elements and prevent duplication
    scene_memory = {
        "scenes": {},
        "settings_used": [],
        "character_states": {},
        "plot_points_covered": [],
        "dialogue_topics": []
    }
    
    # Initialize character states
    for char in [base_inputs['main_character_profile']] + base_inputs['supporting_characters_profile']:
        scene_memory["character_states"][char['name']] = {
            "current_emotional_state": "initial",
            "knowledge_gained": [],
            "relationships": {}
        }
    
    # Create PDF
    pdf = FPDF()
    # Set margins for screenplay format (1.5" left, 1" others)
    pdf.set_margins(38.1, 25.4, 25.4)  # Convert inches to mm
    pdf.set_auto_page_break(True, margin=25.4)
    # Use standard Courier font
    pdf.set_font('Courier', size=12)
    
    # Process each outline point
    for scene_num, outline_text in expanded_outline.items():
        scene_index = int(scene_num.split("_")[1])
        
        # Update inputs with current outline and scene-specific context
        inputs = base_inputs.copy()
        inputs['outline'] = outline_text
        inputs['scene_number'] = scene_num
        inputs['scene_index'] = scene_index
        
        # Add scene progression context
        inputs['previous_scenes'] = {k: v for k, v in scene_memory["scenes"].items()}
        inputs['scene_memory'] = scene_memory
        
        # Add specific narrative position information
        if scene_index > 1:
            inputs['previous_scene'] = scene_memory["scenes"].get(f"scene_{scene_index-1}")
            inputs['previous_scene_outline'] = expanded_outline.get(f"scene_{scene_index-1}")
        else:
            inputs['previous_scene'] = None
            inputs['previous_scene_outline'] = None
            
        if f"scene_{scene_index+1}" in expanded_outline:
            inputs['next_scene_outline'] = expanded_outline.get(f"scene_{scene_index+1}")
        else:
            inputs['next_scene_outline'] = None
        
        # Run crew for this outline point
        result = ActOneBuilder().crew().kickoff(inputs=inputs)
        
        # Save scene result to memory
        scene_memory["scenes"][scene_num] = str(result)
        
        # Parse and update scene memory with new elements
        scene_text = str(result).lower()
        
        # Extract possible settings
        if "INT." in str(result) or "EXT." in str(result):
            for line in str(result).split("\n"):
                if line.strip().startswith(("INT.", "EXT.")):
                    if line.strip() not in scene_memory["settings_used"]:
                        scene_memory["settings_used"].append(line.strip())
        
        # Track dialogue topics (very simplified approach)
        for char in [base_inputs['main_character_profile']['name']] + [c['name'] for c in base_inputs['supporting_characters_profile']]:
            if char.upper() in str(result):
                char_lines = []
                capture = False
                for line in str(result).split("\n"):
                    if char.upper() in line and ":" not in line:
                        capture = True
                    elif capture and line.strip() and any(c.upper() in line and ":" not in line for c in 
                          [base_inputs['main_character_profile']['name']] + [c['name'] for c in base_inputs['supporting_characters_profile']]):
                        capture = False
                    elif capture and line.strip():
                        char_lines.append(line.strip())
                
                # Add dialogue topics to memory (simplified)
                for line in char_lines:
                    topic = f"{char}: {line[:30]}..."
                    if topic not in scene_memory["dialogue_topics"]:
                        scene_memory["dialogue_topics"].append(topic)
        
        # Add page to PDF
        pdf.add_page()
        # Convert result to string and split into lines
        content = str(result)  # Convert CrewOutput to string directly
        lines = content.split('\n')
        for line in lines:
            pdf.multi_cell(0, 5, line.encode('latin-1', 'replace').decode('latin-1'))

    # Save the final PDF
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    print(f"Attempting to save PDF to: {output_dir.absolute()}")
    
    try:
        output_path = output_dir / "act_one_scenes.pdf"
        print(f"Writing PDF to: {output_path}")
        pdf.output(str(output_path), 'F')
        print("PDF generated successfully!")
        
        # Also save scene memory for debugging/analysis
        with open(output_dir / "scene_memory.json", "w") as f:
            # Convert sets to lists for JSON serialization
            memory_json = {
                "scenes": scene_memory["scenes"],
                "settings_used": scene_memory["settings_used"],
                "dialogue_topics": scene_memory["dialogue_topics"],
                "plot_points_covered": scene_memory["plot_points_covered"]
            }
            # Handle character states separately due to nested sets
            char_states_json = {}
            for char, state in scene_memory["character_states"].items():
                char_states_json[char] = {
                    "current_emotional_state": state["current_emotional_state"],
                    "knowledge_gained": state["knowledge_gained"],
                    "relationships": state["relationships"]
                }
            memory_json["character_states"] = char_states_json
            
            json.dump(memory_json, f, indent=2)
            print("Scene memory saved for analysis")
            
    except Exception as e:
        print(f"Error generating PDF: {str(e)}")
        print(f"Error type: {type(e)}")
        # Try alternative encoding
        try:
            # Try encoding the content first
            output_path = output_dir / "act_one_scenes.pdf"
            print("Attempting alternative encoding...")
            pdf.output(str(output_path), 'F')
            print("PDF generated successfully with alternative encoding!")
        except Exception as e:
            print(f"Failed to generate PDF with alternative encoding: {str(e)}")
            print(f"Error type: {type(e)}")
            raise  # This will show the full stack trace

run()