import unittest
from central_message import CentralMessageTool

class TestCentralMessageTool(unittest.TestCase):
    def setUp(self):
        self.tool = CentralMessageTool()
        self.test_logline = "In a high-stakes battle for power and righteousness within the ruling party, loyal Stephen Nedumpally must confront betrayals, navigate treachery, and face off against the corrupt son-in-law to safeguard his principles and the party's future."
        self.test_story_elements = {
            "main_character": "Stephen Nedumpally, a loyal party member with a mysterious past who becomes a pivotal figure in the chaotic power struggle within the ruling party.",
            "primary_mission": "To navigate the treacherous political landscape, uphold his principles, and emerge victorious in the battle for dominance within the party.",
            "up_against": "Stephen faces internal factions within the ruling party vying for power, particularly Bobby, the late leader's corrupt son-in-law who seeks personal gain and poses a significant threat.",
            "at_stake": "Stephen's loyalty, principles, and the future of the party are at stake as he navigates a web of secrets, betrayals, and conspiracies in a high-stakes fight against corruption and for righteousness."
        }

    def test_run_returns_dict(self):
        """Test if _run method returns a dictionary with all required keys"""
        result = self.tool._run(self.test_logline, self.test_story_elements)
        self.assertIsInstance(result, dict)
        self.assertIn('protagonist_belief', result)
        self.assertIn('antagonist_belief', result)
        self.assertIn('central_message', result)

    def test_protagonist_belief_generation(self):
        """Test if protagonist belief is generated correctly"""
        belief = self.tool._generate_protagonist_belief(
            self.test_logline, 
            self.test_story_elements
        )
        self.assertIsInstance(belief, str)
        self.assertTrue(len(belief) > 0)

    def test_antagonist_belief_generation(self):
        """Test if antagonist belief is generated correctly"""
        protagonist_belief = self.tool._generate_protagonist_belief(
            self.test_logline, 
            self.test_story_elements
        )
        antagonist_belief = self.tool._generate_antagonist_belief(
            self.test_logline, 
            self.test_story_elements,
            protagonist_belief
        )
        self.assertIsInstance(antagonist_belief, str)
        self.assertTrue(len(antagonist_belief) > 0)

    def test_central_message_generation(self):
        """Test if central message is generated correctly"""
        protagonist_belief = "Unwavering loyalty and rigid principles are the only path to maintaining order and justice."
        antagonist_belief = "Power and personal gain justify any means, principles are merely obstacles to success."
        central_message = self.tool._generate_central_message(
            protagonist_belief,
            antagonist_belief
        )
        self.assertIsInstance(central_message, str)
        self.assertTrue(len(central_message) > 0)

    def test_error_handling(self):
        """Test if the tool handles errors gracefully"""
        # Test with invalid input
        result = self.tool._run("", {})
        self.assertTrue(isinstance(result, str) and result.startswith("Error"))

def main():
    # Create an instance of the tool
    tool = CentralMessageTool()
    
    # Test data
    test_logline = "In a high-stakes battle for power and righteousness within the ruling party, loyal Stephen Nedumpally must confront betrayals, navigate treachery, and face off against the corrupt son-in-law to safeguard his principles and the party's future."
    test_story_elements = {
        "main_character": "Stephen Nedumpally, a loyal party member with a mysterious past who becomes a pivotal figure in the chaotic power struggle within the ruling party.",
        "primary_mission": "To navigate the treacherous political landscape, uphold his principles, and emerge victorious in the battle for dominance within the party.",
        "up_against": "Stephen faces internal factions within the ruling party vying for power, particularly Bobby, the late leader's corrupt son-in-law who seeks personal gain and poses a significant threat.",
        "at_stake": "Stephen's loyalty, principles, and the future of the party are at stake as he navigates a web of secrets, betrayals, and conspiracies in a high-stakes fight against corruption and for righteousness."
    }

    # Run the tool
    print("Testing CentralMessageTool...")
    print("\nGenerating beliefs and central message...")
    
    result = tool._run(test_logline, test_story_elements)
    
    print("\nResults:")
    print("=" * 50)
    print("Protagonist Belief:")
    print(result['protagonist_belief'])
    print("\nAntagonist Belief:")
    print(result['antagonist_belief'])
    print("\nCentral Message:")
    print(result['central_message'])
    print("=" * 50)

if __name__ == '__main__':
    # Run unit tests
    unittest.main(argv=[''], exit=False)
    
    # Run main demonstration
    print("\nRunning main demonstration...")
    main()