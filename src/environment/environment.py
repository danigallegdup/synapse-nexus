class Environment:
    def __init__(self):
        self.state = None

    def reset(self):
        """Reset the environment."""
        self.state = "Initial state"
        return self.state

    def step(self, action):
        """Apply action and update the environment."""
        pass
