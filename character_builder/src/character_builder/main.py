#!/usr/bin/env python
import sys
import warnings

from character_builder.crew import CharacterBuilder

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
        
    "abstract": "Set against the backdrop of the affluent Palamattathu family, Christian Brothers follows the lives of two brothers, Christy  and Joji . Christy, a high-profile police informant in Mumbai, becomes estranged from his family due to misconceptions about his profession. Meanwhile, Joji abandons his theological studies in Italy after falling in love with Meenakshi, the daughter of a state minister. The family's patriarch, Varghese Mappila (Saikumar), faces turmoil when internal conflicts and external threats jeopardize their unity and legacy. The narrative intertwines themes of love, betrayal, and the quest for justice, culminating in a family's struggle to stay united amidst chaos.The family finally comes together to face against george kutty who is christys brother in law who tries to trap christy in a false case",
    "logline": " In the face of betrayal and external threats, two estranged brothers must reconcile their differences to protect their family's legacy and seek justice.",
    "central_message": "The film explores themes of familial bonds, loyalty, and redemption. It delves into the complexities of family relationships, highlighting how misunderstandings and external influences can strain ties, and emphasizes the importance of trust and unity in overcoming adversities.",
    "character_details": "Christy the protagonist is the eldest son of palamatil house who is bank maager turned to goon.George Kutty who is the Antagonist is Christrys brother in law he is a a smuggler and want to destroy everyone.Joji who christys youngest brother is a romantic guy who marries meenakshy and is also a priest who didnt succesfully come out as priest.Captain Varghese Mapala is christys father and is a retired captain of indian army.Meenakshy is the daughter of Kerala home minister  and fall in love with joji",
}

    
    CharacterBuilder().crew().kickoff(inputs=inputs)

run()