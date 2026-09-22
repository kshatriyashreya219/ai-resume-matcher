class MatcherAgent:
    def match(self, resume_data, jd):
        skills=resume_data.get("skills",[])
        matched=[s for s in skills if s.lower() in jd.lower()]
        score=len(matched)*25
        return {"match_score": min(score,95), "matched_skills": matched}
