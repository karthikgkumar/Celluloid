from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
load_dotenv()
# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ActOneBuilder():
    """ActOneBuilder crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def act_one_plot_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['act_one_plot_architect'],
            verbose=True
        )

    @agent
    def act_one_scene_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['act_one_scene_architect'],
            verbose=True
        )

    @agent
    def act_one_dialogue_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['act_one_dialogue_specialist'],
            verbose=True
        )

    @agent
    def act_one_character_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['act_one_character_architect'],
            verbose=True
        )

    @agent
    def act_one_world_builder(self) -> Agent:
        return Agent(
            config=self.agents_config['act_one_world_builder'],
            verbose=True
        )

    @agent
    def act_one_integration_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['act_one_integration_manager'],
            verbose=True
        )

    # @task
    # def outline_creation_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['outline_creation_task']
    #     )

    @task
    def plot_structure_task(self) -> Task:
        return Task(
            config=self.tasks_config['plot_structure_task']
        )

    @task
    def scene_development_task(self) -> Task:
        return Task(
            config=self.tasks_config['scene_development_task']
        )

    @task
    def dialogue_development_task(self) -> Task:
        return Task(
            config=self.tasks_config['dialogue_development_task']
        )

    @task
    def character_introduction_task(self) -> Task:
        return Task(
            config=self.tasks_config['character_introduction_task']
        )

    @task
    def world_building_task(self) -> Task:
        return Task(
            config=self.tasks_config['world_building_task']
        )

    @task
    def integration_task(self) -> Task:
        return Task(
            config=self.tasks_config['integration_task']
        )

    @task
    def quality_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['quality_review_task']
        )

    @task
    def final_assembly_task(self) -> Task:
        return Task(
            config=self.tasks_config['final_assembly_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ActOneBuilder crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
