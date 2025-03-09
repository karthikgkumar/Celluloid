
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
    
    @agent
    def scene_memory_tracker(self) -> Agent:
        return Agent(
            config=self.agents_config['scene_memory_tracker'],
            verbose=True
        )
    
    @agent
    def workflow_controller(self) -> Agent:
        return Agent(
            config=self.agents_config['workflow_controller'],
            verbose=True
        )
    
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
    def scene_memory_tracking_task(self) -> Task:
        return Task(
            config=self.tasks_config['scene_memory_tracking_task']
        )
    
    @task
    def integration_task(self) -> Task:
        return Task(
            config=self.tasks_config['integration_task']
        )
    
    @task
    def workflow_control_task(self) -> Task:
        return Task(
            config=self.tasks_config['workflow_control_task']
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
        """Creates the ActOneBuilder crew with a modified process to ensure scene uniqueness"""
        return Crew(
            agents=self.agents,
            tasks=[
                # First, understand the scene's position in the narrative
                self.workflow_control_task(),
                
                # Create the basic structure with awareness of previous scenes
                self.plot_structure_task(),
                
                # Develop distinct scene elements
                self.scene_development_task(),
                self.world_building_task(),
                self.character_introduction_task(),
                self.dialogue_development_task(),
                
                # Track and verify scene uniqueness
                self.scene_memory_tracking_task(),
                
                # Integration and quality checks
                self.integration_task(),
                self.quality_review_task(),
                
                # Final assembly with uniqueness verification
                self.final_assembly_task()
            ],
            process=Process.sequential,  # Using sequential to ensure proper progression
            verbose=True,
        )
    
    # Optional: Add custom methods to help with scene uniqueness tracking
    def before_kickoff(self, inputs):
        """Initialize scene memory if not present"""
        if 'scene_memory' not in inputs:
            inputs['scene_memory'] = {
                "scenes": {},
                "settings_used": set(),
                "character_states": {},
                "plot_points_covered": set(),
                "dialogue_topics": set()
            }
            
            # Initialize character states
            for char in [inputs['main_character_profile']] + inputs['supporting_characters_profile']:
                char_name = char['name'] if isinstance(char, dict) else char
                inputs['scene_memory']["character_states"][char_name] = {
                    "current_emotional_state": "initial",
                    "knowledge_gained": set(),
                    "relationships": {}
                }
        
        # Ensure scene position is clear
        scene_num = inputs.get('scene_number', 'unknown')
        print(f"\n=== Processing Scene {scene_num} ===")
        print(f"Outline: {inputs.get('outline', '')[:100]}...")
        
        return inputs
    
    def after_kickoff(self, result, inputs):
        """Update scene memory with the latest scene content"""
        scene_num = inputs.get('scene_number', 'unknown')
        scene_memory = inputs.get('scene_memory', {})
        
        # Store the scene result
        if 'scenes' in scene_memory:
            scene_memory['scenes'][scene_num] = str(result)
            
        print(f"\n=== Completed Scene {scene_num} ===")
        print(f"Length: {len(str(result))} characters")
        
        return result