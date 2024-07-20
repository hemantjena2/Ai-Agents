import google.generativeai as genai

class MasterAgent:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def process_query(self, query):
        prompt = f"""Analyze this query and decide which agent should handle it: "{query}"

        Available agents and their responsibilities:
        1. TutorAgent: Handles student profiles, interests, and background information
        2. LearningTrackingAgent: Manages learning progress, assessments, and knowledge testing
        3. RoadmapAgent: Creates personalized learning paths and course structures
        4. CoachAgent: Provides explanations, feedback, and detailed subject matter assistance

        Rules for agent selection:
        - If the query is about personal interests, profile, or background, choose TutorAgent
        - If the query is about testing knowledge or tracking progress, choose LearningTrackingAgent
        - If the query is about creating a learning plan or path, choose RoadmapAgent
        - If the query is asking for explanations or specific subject matter help, choose CoachAgent

        Respond with only one of these agent names."""
        
        response = self.model.generate_content(prompt)
        return response.text.strip()