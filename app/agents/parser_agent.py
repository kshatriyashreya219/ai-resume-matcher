import PyPDF2
class ParserAgent:
    def parse(self, path: str):
        text=""
        with open(path, 'rb') as f:
            r=PyPDF2.PdfReader(f)
            for p in r.pages:
                text+=p.extract_text() or ""
        skills=["Python","FastAPI","SQL","Machine Learning","React","Java","OpenCV","YOLO"]
        found=[s for s in skills if s.lower() in text.lower()]
        return {"raw_text": text, "skills": found}
