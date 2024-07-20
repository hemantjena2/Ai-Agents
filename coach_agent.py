import google.generativeai as genai

class CoachAgent:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def explain_course(self, course, student_profile):
        prompt = f"Explain the course '{course}' tailored to this student profile: {student_profile}"
        response = self.model.generate_content(prompt)
        return response.text

    def provide_feedback(self, student_performance):
        prompt = f"Provide coaching feedback based on this student performance: {student_performance}"
        response = self.model.generate_content(prompt)
        return response.text