from agent import Agent

class RLAgent(Agent):
    def __init__(self, name, policy):
        super().__init__(name)
        self.policy = policy

    def act(self, state):
        """Use policy to decide action."""
        return self.policy(state)
