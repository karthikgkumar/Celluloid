#!/usr/bin/env pytho
from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start

from crews.poem_crew.poem_crew import PoemCrew
from dotenv import load_dotenv

load_dotenv()

class CelluloidState(BaseModel):
    sentence_count: int = 1
    poem: str = ""


class CelluloidFlow(Flow[CelluloidState]):
    inputs = {
        "abstract": """The movie revolves around the intense political drama that unfolds following the death of a state's Chief Minister. The story explores the chaotic power struggle within the ruling party, where various factions with their own agendas battle for dominance. Central to the narrative is a character named Stephen Nedumpally, a loyal party member with a mysterious past, who emerges as a pivotal figure in the conflict.

On the other side, there's Bobby, the late leader's son-in-law, who harbors corrupt intentions and seeks to exploit the situation for personal gain. As the power struggle intensifies, secrets, betrayals, and conspiracies come to light, creating a gripping tale of politics, loyalty, and the fight against corruption. The film delves into themes of morality, power, and the price of righteousness, all while delivering high-octane action and emotional depth.

This concept sets the stage for a compelling political action thriller with plenty of twists, dramatic character arcs, and a climactic reveal of the protagonist's true motives. It could also lay the foundation for sequels, exploring the protagonist's backstory and the consequences of the events in the first installment.""",
    }

    @start()
    def generate_sentence_count(self):
        print("Generating sentence count")

    @listen(generate_sentence_count)
    def generate_celluloid(self):
        print("Generating celluloid")
        result = (
            PoemCrew()
            .crew()
            .kickoff(inputs={
                "sentence_count": self.state.sentence_count,
                "abstract": self.inputs["abstract"]
            })
        )

        print("Poem generated", result.raw)
        self.state.poem = result.raw

    @listen(generate_celluloid)
    def save_celluloid(self):
        print("Saving celluloid")
        with open("celluloid.txt", "w") as f:
            f.write(self.state.poem)


def kickoff():
    celluloid_flow = CelluloidFlow()
    celluloid_flow.kickoff()


# def plot():
#     celluloid_flow = CelluloidFlow()
#     celluloid_flow.plot()


if __name__ == "__main__":
    kickoff()
