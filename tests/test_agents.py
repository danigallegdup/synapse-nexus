import unittest
from src.agents.agent import Agent

class TestAgent(unittest.TestCase):
    def test_initialization(self):
        agent = Agent("TestAgent")
        self.assertEqual(agent.name, "TestAgent")
