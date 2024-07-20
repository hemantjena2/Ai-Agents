import google.generativeai as genai

class LearningTrackingAgent:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def generate_question(self, topic):
        prompt = f"Generate a question about {topic}"
        response = self.model.generate_content(prompt)
        return response.text

    def evaluate_answer(self, question, answer):
        prompt = f"Evaluate this answer to the question '{question}': {answer}"
        response = self.model.generate_content(prompt)
        return response.text

    def create_summary(self, topic, performance):
        prompt = f"Create a learning summary for {topic} based on this performance: {performance}"
        response = self.model.generate_content(prompt)
        return response.text