from fastapi import APIRouter, UploadFile, File, Form
import shutil, os
from app.agents.parser_agent import ParserAgent
from app.agents.matcher_agent import MatcherAgent
from app.agents.interview_agent import InterviewAgent
router=APIRouter()
parser, matcher, interviewer = ParserAgent(), MatcherAgent(), InterviewAgent()
@router.post("/analyze")
async def analyze_resume(resume: UploadFile = File(...), job_description: str = Form(...)):
    temp=f"temp_{resume.filename}"
    with open(temp, "wb") as b:
        shutil.copyfileobj(resume.file, b)
    rd=parser.parse(temp)
    mr=matcher.match(rd, job_description)
    qs=interviewer.get_questions(rd, job_description, mr)
    os.remove(temp)
    return {"skills": rd["skills"], "match": mr, "questions": qs}
