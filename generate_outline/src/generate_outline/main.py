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
    'abstract': """A gritty investigative thriller about a journalist who uncovers 
                  a conspiracy involving corporate corruption and murder, forcing him 
                  to confront his own demons while pursuing the truth.""",
    
    'logline': """A troubled investigative journalist must navigate a web of corporate 
                  corruption and personal demons to expose a powerful businessman's 
                  murderous secret before more lives are lost.""",
    
    'central_message': """The pursuit of truth requires confronting both external 
                         corruption and internal darkness.""",
    
    'main_character_profile': """
    Name: Ethan Cole
    Age: 35
    Occupation: Investigative Journalist
    Personality: Intelligent, obsessive, morally conflicted
    Background: Ethan grew up in a rough neighborhood, using his sharp mind to escape 
                a life of crime. He gained fame for uncovering high-profile scandals 
                but struggles with past trauma and a drinking problem.
    Motivation: Determined to expose corruption, but haunted by a past case that went 
                horribly wrong.
    Character Arc: Ethan starts as a lone wolf who trusts no one, but through his 
                  latest case, he learns the value of connection and truth over 
                  sensationalism.
    Flaws: Stubborn, reckless, prone to self-destruction.
    Strengths: Sharp intuition, relentless pursuit of the truth.
    """,
    
    'supporting_characters_profile': """
    1. Dr. Lillian Graves (Psychologist, 40s)
       - Ethan's therapist, intelligent but emotionally guarded
       - She holds a secret about Ethan's past that could break him

    2. Marcus "Mack" DeLuca (Cop, 50s)
       - Ethan's reluctant ally, a veteran detective who has seen too much
       - He helps Ethan navigate the criminal underworld but warns him not to push too far

    3. Sophia Reyes (Tech Specialist, 28)
       - A hacker who helps Ethan dig into classified files
       - Sarcastic, street-smart, and secretly on the run from her own past

    4. Vincent Kane (Antagonist, 45)
       - A powerful businessman hiding a dark secret
       - He manipulates the media and law enforcement to cover up crimes
    """,
    
    'genre': "Investigative Thriller"
}
    GenerateOutline().crew().kickoff(inputs=inputs)

run()

#OUTPUT
## Final Answer:
# yaml
# act_one:
#   opening_scene:
#     - Ethan Cole is introduced in a bustling city newsroom, a place rife with ambition and fraught with tension. A montage of his previous investigative successes hints at his reputation, yet a dark undertone reveals his struggles with alcohol and trauma. A loud argument over a shady corporate deal in the background foreshadows the intrigue to 
# come.

#   opportunity:
#     description:
#       - Ethan receives an anonymous tip about a high-ranking businessman, Vincent Kane, who was involved in a suspicious workplace accident that resulted in a worker's death. The tip hints at a cover-up that will link the death to embezzlement and corporate corrupt practices.
#     character_impact:
#       - This opportunity sparks Ethan's obsessive nature, igniting old instincts and springing him into action. He reflects on his past failures, which resurfaces his fears 
# of inadequacy.
#     story_launch:
#       - Driven by the promise of unveiling a mighty conspiracy, Ethan decides to investigate Kane, breaking the icy isolation he’s built around himself.

#   new_situation:
#     adaptation:
#       - Ethan begins to gather evidence through interviews with disgruntled former employees and exploring Kane’s corporate ties. His work re-establishes some of his old connections, including Sophia, who reluctantly agrees to help.
#     stakes:
#       - As Ethan digs deeper, he finds evidence of further potential murders linked to Kane, setting heightened stakes beyond just career dissatisfaction.
#     goal_definition:
#       - Ethan’s new goal is to connect the dots between the workplace accident, the ensuing cover-up, and the shadowy dealings of Vincent Kane to expose the truth without succumbing to his demons.

# act_two:
#   change_of_plans:
#     complication:
#       - A high-profile journalist steals Ethan's lead, publishing a sensationalized version of the story which discredits Ethan's findings, making it harder for him to gain 
# traction.
#     goal_revision:
#       - Faced with this setback, Ethan recalibrates his focus to not only unearth the truth but to expose the corruption behind the media manipulation and solidify his credibility.
#     character_challenge:
#       - This setback tests Ethan's resolve and rekindles his self-destructive drinking habits. His reliance on allies becomes crucial but also poses risks as they are just as vulnerable as he is.

#   progress:
#     escalation:
#       - Ethan, with Sophia’s tech skills, hacks into Kane's secure corporate communications. They uncover a web of illicit activities, leading them to witness a murder committed to silence a whistleblower.
#     character_growth:
#       - Ethan starts to realize that he cannot solve everything alone. He reluctantly reaches out to Mack, who aids him in navigating police hostility towards Ethan's pursuits.
#     subplot_integration:
#       - The tension increases as Mack reveals his own professional corruption dilemmas, paralleling Ethan’s internal battles and emphasizing the story’s themes.

#   point_of_no_return:
#     critical_choice:
#       - After discovering the depth of Kane's corruption and realizing his own past mistakes, Ethan must choose between going public with the information, risking lives, or 
# protecting his newfound friends.
#     commitment:
#       - Ethan decides to go all-in with the investigation, aligning his aims with those of Mack and Sophia despite the personal risks involved.
#     stakes_elevation:
#       - This choice heightens personal stakes as threats against Ethan’s life are made directly by Kane’s henchmen, compelling him into hiding.

#   raising_stakes:
#     conflicts:
#       - Ethan faces growing hostility from both Kane’s corporate staff, who try to discredit him, and police, who warn him to back off, highlighting a conspiracy that extends to law enforcement.
#     obstacles:
#       - As Ethan collects proof, he struggles against both internal pressures from his trauma and external pressures from those trying to silence him.
#     character_pressure:
#       - Increasing paranoia sets in as Ethan finds it difficult to trust even Mack and Sophia while wrestling with his addiction; his vulnerability escalates the tension.   

#   lowest_point:
#     crisis:
#       - In a climactic moment, Ethan’s attempts to publish his findings lead to a personal loss—one of his closest allies is killed in retaliation for their investigation.  
#     character_break:
#       - The betrayal shatters Ethan's fragile emotional state, pushing him towards a breakdown and a near fatal relapse into alcoholism.
#     setup_resolution:
#       - The tragedy forces Ethan to confront his addiction openly, leading back to Dr. Lillian Graves who reveals long-buried truths about Ethan’s past that reshape his perception of himself.

# act_three:
#   final_conflict:
#     climax:
#       - Armed with new conviction and emotional clarity, Ethan confronts Kane at a public corporate gala, where he unveils the evidence of murder and corruption in front of 
# press and authorities.
#     character_test:
#       - Ethan must stand firm, facing the embodiment of all he fears, Kane, as well as the very tactics he abhors—media manipulation, threats, and violence.
#     theme_culmination:
#       - Ethan realizes that bringing the truth to light requires embracing vulnerability and the connections he has formed; he unites his allies in exposing Kane together.  

#   conclusion:
#     resolution:
#       - With Kane arrested and his crimes exposed, Ethan’s articles spark a massive surge against corporate corruption. He restores his credibility and begins to heal from his past.
#     character_arc:
#       - Ethan transforms from a reluctant lone wolf into a cooperative journalist who values the connections formed through trust in his allies, embracing life beyond the thrill of the chase.
#     theme_resolution:
#       - The story closes with a meditation on truth-seeking, the necessity of community and trust, and the idea that facing our demons is a necessary step in challenging corruption within ourselves and society.
######################################################################################################################################
# Agent: Investigative Thriller Story Structure Analyst and Script Consultant
## Final Answer:
# yaml
# structure_assessment: {
#   act_one_evaluation:
#     - The opening scene effectively introduces Ethan's character and sets up the central conflict with corporate corruption. The montage of his investigative successes contrasts with his personal struggles, creating a strong foundation for his journey. The foreshadowing through a background argument enhances intrigue and reflects the tension within his world.

#   act_two_evaluation:
#     - The act two progression is compelling, featuring a clear complication (the high-profile journalist stealing Ethan's lead), which raises stakes and tests his resolve. The escalation through Ethan's hacking into Kane's communications and the murder reveal is effective in propelling the tension. Character development occurs with Ethan's increasing reliance on Sophia and Mack, demonstrating his evolution despite his inner demons.

#   act_three_evaluation:
#     - The climax at the corporate gala is impactful, with Ethan's confrontation of Kane allowing for both dramatic tension and thematic resolution. The culmination of his personal growth and the necessity of seeking truth through vulnerability is well-articulated. The resolution of Kane's arrest and the restoration of Ethan's credibility offer 
# a satisfying conclusion to the narrative arc.

#   pacing_analysis:
#     - Overall, the pacing is well-maintained with clear thematic beats aligned with character development. However, certain sections could benefit from heightened tension, particularly in act two where Ethan's addiction challenges could be placed more strategically to amplify urgency leading into the lowest point.
# }

# character_development: {
#   arc_progression:
#     - Ethan's transformation from a solitary journalist to one who values connections is effectively illustrated through his interactions with Sophia and Mack. Each character teaches Ethan about trust, collaboration, and the consequences of his choices.

#   motivation_clarity:
#     - Ethan's motivations remain clear and driven throughout the script. His past trauma and obsession with exposing the truth are coherent, aligning well with his character flaws and development.

#   conflict_impact:
#     - The varied external challenges Ethan faces - from corporate threats to media manipulation - effectively counterbalance his internal struggles with addiction and trauma, providing a layered conflict that enhances character growth.
# }

# theme_integration: {
#   message_delivery:
#     - The central message of confronting both external and internal corruption is clear throughout the narrative. The portrayal of truth-seeking intertwined with personal demons ensures consistent thematic exploration.

#   subplot_alignment:
#     - Supporting characters like Mack and Sophia embody various facets of corruption and redemption, reinforcing Ethan's journey. Their individual arcs parallel and intersect with Ethan's, enhancing the main theme of trust and truth.

#   resolution_effectiveness:
#     - The thematic payoff is strong with Ethan finally realizing that vulnerability and trust are keys to his success. The closing reflection on truth-seeking wraps up the exploration of the themes, leaving the audience with a profound sense of the importance of confronting one's darkness.
# }

# improvement_recommendations: {
#   structural_adjustments:
#     - Consider sharpening the pacing in act two by weaving in more immediate consequences for Ethan's addiction to deepen the sense of urgency. A moment where his knowledge 
# of the cover-up inadvertently leads to a setback could heighten tension.

#   character_enhancements:
#     - Further develop Dr. Lillian Graves’s role to maximize her impact on Ethan’s arc. Perhaps revealing more of her personal struggles or intertwining elements of her own secret with Ethan's journey can deepen emotional stakes.

#   pacing_optimization:
#     - Introduce brief moments of respite within high-intensity sequences to allow audiences to breathe, enhancing emotional weight. This would create a rhythm that allows for tension buildup coupled with moments of vulnerability among characters.
# }