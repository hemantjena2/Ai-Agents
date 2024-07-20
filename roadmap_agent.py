import google.generativeai as genai

class RoadmapAgent:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def create_learning_path(self, topic, student_profile):
        prompt = f"Create a personalized learning path for {topic} based on this student profile: {student_profile}"
        response = self.model.generate_content(prompt)
        return response.text