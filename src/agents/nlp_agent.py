from transformers import pipeline

class NLPAgent:
    def __init__(self):
        self.model = pipeline("text-generation", model="gpt-2")

    def generate_response(self, prompt):
        """Generate a natural language response."""
        return self.model(prompt)
