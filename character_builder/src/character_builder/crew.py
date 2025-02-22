from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class CharacterBuilder():
    """CharacterBuilder crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def character_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['character_analyzer'],
            verbose=True
        )

    @agent 
    def moral_weakness_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['moral_weakness_developer'],
            verbose=True
        )

    @agent
    def physical_trait_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['physical_trait_designer'],
            verbose=True
        )

    @agent
    def desire_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['desire_architect'],
            verbose=True
        )

    @agent
    def self_deception_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['self_deception_analyst'],
            verbose=True
        )

    @agent
    def character_needs_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['character_needs_developer'],
            verbose=True
        )

    @agent
    def dialogue_personality_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['dialogue_personality_writer'],
            verbose=True
        )

    @agent
    def character_profile_assembler(self) -> Agent:
        return Agent(
            config=self.agents_config['character_profile_assembler'],
            verbose=True
        )

    @task
    def analyze_character_inputs(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_character_inputs']
        )

    @task
    def define_moral_weaknesses(self) -> Task:
        return Task(
            config=self.tasks_config['define_moral_weaknesses']
        )

    @task
    def design_physical_traits(self) -> Task:
        return Task(
            config=self.tasks_config['design_physical_traits']
        )

    @task
    def develop_character_desires(self) -> Task:
        return Task(
            config=self.tasks_config['develop_character_desires']
        )

    @task
    def identify_self_deceptions(self) -> Task:
        return Task(
            config=self.tasks_config['identify_self_deceptions']
        )

    @task
    def determine_character_needs(self) -> Task:
        return Task(
            config=self.tasks_config['determine_character_needs']
        )

    @task
    def create_signature_dialogue(self) -> Task:
        return Task(
            config=self.tasks_config['create_signature_dialogue']
        )

    @task
    def assemble_character_profiles(self) -> Task:
        return Task(
            config=self.tasks_config['assemble_character_profiles']
        )

    @task
    def validate_character_arcs(self) -> Task:
        return Task(
            config=self.tasks_config['validate_character_arcs']
        )

    @task
    def ensure_thematic_alignment(self) -> Task:
        return Task(
            config=self.tasks_config['ensure_thematic_alignment']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CharacterBuilder crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
