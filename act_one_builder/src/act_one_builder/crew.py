from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
load_dotenv()

@CrewBase
class ActOneBuilder():
    """ActOneBuilder crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    @agent
    def story_outline_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['story_outline_architect'],
            verbose=True
        )
    
    @agent 
    def scene_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['scene_writer'],
            verbose=True
        )
    
    @agent
    def dialogue_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['dialogue_specialist'],
            verbose=True
        )
    
    @agent
    def continuity_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['continuity_manager'],
            verbose=True
        )
    
    @agent
    def format_validator(self) -> Agent:
        return Agent(
            config=self.agents_config['format_validator'],
            verbose=True
        )
    
    @task
    def story_outline_task(self) -> Task:
        return Task(
            config=self.tasks_config['story_outline_task']
        )
    
    @task
    def scene_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['scene_writing_task']
        )
    
    @task
    def dialogue_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['dialogue_creation_task']
        )
    
    @task
    def continuity_tracking_task(self) -> Task:
        return Task(
            config=self.tasks_config['continuity_tracking_task']
        )
    
    @task
    def format_validation_task(self) -> Task:
        return Task(
            config=self.tasks_config['format_validation_task']
        )
    
    @task
    def integration_task(self) -> Task:
        return Task(
            config=self.tasks_config['integration_task']
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the ActOneBuilder crew"""
        return Crew(
            agents=self.agents,
            tasks=[
                # Create story outline
                self.story_outline_task(),
                
                # Write and format scenes
                self.scene_writing_task(),
                self.dialogue_creation_task(),
                
                # Validate and integrate
                self.continuity_tracking_task(),
                self.format_validation_task(),
                self.integration_task()
            ],
            process=Process.sequential,
            verbose=True,
        )
    
    def before_kickoff(self, inputs):
        """Initialize screenplay tracking"""
        print("\n=== Starting Screenplay Generation ===")
        print(f"Genre: {inputs.get('genre', '')}")
        print(f"Logline: {inputs.get('logline', '')[:100]}...")
        return inputs
    
    def after_kickoff(self, result, inputs):
        """Final screenplay validation"""
        print("\n=== Screenplay Generation Complete ===")
        print(f"Length: {len(str(result))} characters")
        return result