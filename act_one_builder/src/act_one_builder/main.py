#!/usr/bin/env python
import sys
import warnings
from fpdf import FPDF
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
        "abstract": "A gritty investigative thriller about a journalist who uncovers a conspiracy involving corporate corruption and murder, forcing him to confront his own demons while pursuing the truth.",
        
        "logline": "A troubled investigative journalist must navigate a web of corporate corruption and personal demons to expose a powerful businessman's murderous secret before more lives are lost.",
        
        "central_message": "The pursuit of truth requires confronting both external corruption and internal darkness.",
        
        "main_character_profile": {
            "name": "Ethan Cole",
            "age": 35,
            "occupation": "Investigative Journalist",
            "personality": "Intelligent, obsessive, morally conflicted",
            "background": "Ethan grew up in a rough neighborhood, using his sharp mind to escape a life of crime. He gained fame for uncovering high-profile scandals but struggles with past trauma and a drinking problem.",
            "motivation": "Determined to expose corruption, but haunted by a past case that went horribly wrong.",
            "character_arc": "Ethan starts as a lone wolf who trusts no one, but through his latest case, he learns the value of connection and truth over sensationalism.",
            "flaws": "Stubborn, reckless, prone to self-destruction",
            "strengths": "Sharp intuition, relentless pursuit of the truth"
        },
        
        "supporting_characters_profile": [
            {
                "name": "Dr. Lillian Graves",
                "role": "Psychologist",
                "age": "40s", 
                "description": "Ethan's therapist, intelligent but emotionally guarded",
                "secret": "She holds a secret about Ethan's past that could break him"
            },
            {
                "name": "Marcus 'Mack' DeLuca",
                "role": "Cop",
                "age": "50s",
                "description": "Ethan's reluctant ally, a veteran detective who has seen too much",
                "relationship": "He helps Ethan navigate the criminal underworld but warns him not to push too far"
            },
            {
                "name": "Sophia Reyes",
                "role": "Tech Specialist",
                "age": 28,
                "description": "A hacker who helps Ethan dig into classified files",
                "background": "Sarcastic, street-smart, and secretly on the run from her own past"
            },
            {
                "name": "Vincent Kane",
                "role": "Antagonist", 
                "age": 45,
                "description": "A powerful businessman hiding a dark secret",
                "methods": "He manipulates the media and law enforcement to cover up crimes"
            }
        ],
        "outline": {
                "opening_scene": "Establish Ethan Cole sitting in a dimly lit bar, narrating his troubled past as he struggles with a drink in hand. Flashbacks show his childhood in a rough neighborhood and his rise as an investigative journalist, emphasizing his intelligence and obsession with truth.",
                "opportunity": {
                    "description": "Ethan receives an anonymous tip about a corporate cover-up involving Vincent Kane's company that leads to several unexplained disappearances and potential murders.",
                    "character_impact": "This tip reignites Ethan's drive to expose corruption but also raises the specter of his past failures, drawing him dangerously close to his old habits.",
                    "story_launch": "The tip serves as the inciting incident that propels Ethan into an underworld of corporate crime and personal struggle, setting off the primary plot of the screenplay."
                },
                "new_situation": {
                    "adaptation": "Ethan reluctantly decides to team up with Sophia, a tech specialist, using her hacking skills to dig deeper into Kane's operations while navigating his mistrust.",
                    "stakes": "The initial conflict becomes clear as Ethan's investigations attract dangerous attention, forcing him to evade both corporate thugs and the law.",
                    "goal_definition": "Ethan's objective is now firmly defined: uncover the truth behind the conspiracy and bring Vincent Kane to justice while battling his own inner demons."
                }
        },
        
        "genre": "Investigative Thriller"
    }
    
    # Run the crew and get output
    output = ActOneBuilder().crew().kickoff(inputs=inputs)
    
    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Write screenplay content to PDF - split into lines and encode properly
    lines = str(output).split('\n')
    for line in lines:
        # Encode with latin-1 to handle special characters
        encoded_line = line.encode('latin-1', 'replace').decode('latin-1')
        pdf.multi_cell(0, 5, txt=encoded_line)
    
    # Save the PDF
    pdf.output("screenplay.pdf")

run()