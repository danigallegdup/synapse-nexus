import unittest
from src.environment.environment import Environment

class TestEnvironment(unittest.TestCase):
    def test_reset(self):
        env = Environment()
        state = env.reset()
        self.assertEqual(state, "Initial state")
