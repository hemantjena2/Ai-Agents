import google.generativeai as genai

class TutorAgent:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def update_student_profile(self, student_id, new_info):
        # In a real implementation, this would update a database
        print(f"Updating profile for student {student_id} with info: {new_info}")

    def get_student_interests(self, student_id):
        # In a real implementation, this would retrieve from a database
        student_info = f"Student {student_id} info: age 20, studying computer science"
        prompt = f"Based on this student info, what are their main interests? {student_info}"
        response = self.model.generate_content(prompt)
        return response.text