from master_agent import MasterAgent
from tutor_agent import TutorAgent
from learning_tracking_agent import LearningTrackingAgent
from roadmap_agent import RoadmapAgent
from coach_agent import CoachAgent

class EducationalAISystem:
    def __init__(self, api_key):
        self.master_agent = MasterAgent(api_key)
        self.tutor_agent = TutorAgent(api_key)
        self.learning_tracking_agent = LearningTrackingAgent(api_key)
        self.roadmap_agent = RoadmapAgent(api_key)
        self.coach_agent = CoachAgent(api_key)

    def process_request(self, request, student_id):
        assigned_agent = self.master_agent.process_query(request)
        print(f"Assigned agent: {assigned_agent}")
        
        if assigned_agent == "TutorAgent":
            interests = self.tutor_agent.get_student_interests(student_id)
            print(f"Student interests: {interests}")
        elif assigned_agent == "LearningTrackingAgent":
            question = self.learning_tracking_agent.generate_question("Python")
            print(f"Generated question: {question}")
        elif assigned_agent == "RoadmapAgent":
            path = self.roadmap_agent.create_learning_path("Python", f"Student ID: {student_id}")
            print(f"Learning path: {path}")
        elif assigned_agent == "CoachAgent":
            feedback = self.coach_agent.explain_course("Python", f"Student ID: {student_id}")
            print(f"Course explanation: {feedback}")
        else:
            print(f"Unknown agent: {assigned_agent}")

# The rest of your main.py file remains the same
if __name__ == "__main__":
    api_key = "Your_api_key"  # Replace with your actual Gemini API key
    system = EducationalAISystem(api_key)
    system.process_request("Explain object-oriented programming", "student123")
