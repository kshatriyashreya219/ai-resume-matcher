class InterviewAgent:
    def get_questions(self, resume_data, jd, match_data):
        s=resume_data.get("skills",["Python"])[0]
        return [f"Explain project using {s}?", f"How does {s} fit this JD?", "FastAPI vs Flask?", "How to improve matcher?", "Toughest bug fixed?"]
