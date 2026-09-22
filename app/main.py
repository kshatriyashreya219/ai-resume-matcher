from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from app.api.routes import router
import os

app = FastAPI(title="AI Resume Matcher")

app.include_router(router, prefix="/api")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(BASE_DIR, "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def home():
    # Serve frontend template directly
    if os.path.exists(TEMPLATE_PATH):
        return FileResponse(TEMPLATE_PATH)
    else:
        return HTMLResponse("<h1>API is running. Visit /docs for API docs</h1>")

@app.get("/health")
def health():
    return {"status": "ok"}