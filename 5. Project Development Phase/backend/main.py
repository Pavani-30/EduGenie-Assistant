"""
EduGenie - Google Gemini Powered Learning Assistant
FastAPI backend entry point.

Routes each user action to its module, exactly as shown in the
Technical Architecture diagram:

Start -> Frontend: User Input -> FastAPI Backend (router)
      -> Explanation Module   (/explain)
      -> Q&A Module           (/qa)
      -> Quiz Generation      (/quiz)
      -> Summarization Module (/summarize)
      -> Learning Path Module (/learn/recommendations)
      -> Frontend: Display Results -> End
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv

from modules import explain, qa, quiz, summarize, learning_path
from modules.schemas import (
    ExplainRequest,
    QARequest,
    QuizRequest,
    SummarizeRequest,
    LearningPathRequest,
)

load_dotenv()

app = FastAPI(
    title="EduGenie - Google Gemini Powered Learning Assistant",
    description="A lightweight AI-powered educational assistant built with FastAPI + Google Gemini.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "..", "frontend")
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


@app.get("/")
def serve_frontend():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "EduGenie"}


# ---- Explanation Module ----
@app.post("/explain")
def explain_concept(payload: ExplainRequest):
    try:
        return {"result": explain.get_explanation(payload.topic, payload.level)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


# ---- Q&A Module ----
@app.post("/qa")
def answer_question(payload: QARequest):
    try:
        return {"result": qa.get_answer(payload.question)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


# ---- Quiz Generation Module ----
@app.post("/quiz")
def generate_quiz(payload: QuizRequest):
    try:
        return {"result": quiz.generate_quiz(payload.topic, payload.num_questions)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


# ---- Summarization Module ----
@app.post("/summarize")
def summarize_text(payload: SummarizeRequest):
    try:
        return {"result": summarize.summarize_text(payload.text)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


# ---- Learning Path Module ----
@app.post("/learn/recommendations")
def learning_path_recommendation(payload: LearningPathRequest):
    try:
        return {"result": learning_path.get_learning_path(payload.topic)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
