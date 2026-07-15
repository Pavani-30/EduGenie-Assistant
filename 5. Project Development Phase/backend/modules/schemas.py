from pydantic import BaseModel, Field


class ExplainRequest(BaseModel):
    topic: str = Field(..., example="Pythagoras Theorem")
    level: str = Field("beginner", example="beginner")


class QARequest(BaseModel):
    question: str = Field(..., example="Which is the largest ocean?")


class QuizRequest(BaseModel):
    topic: str = Field(..., example="Pythagoras Theorem")
    num_questions: int = Field(5, ge=1, le=20)


class SummarizeRequest(BaseModel):
    text: str = Field(..., example="Paste a paragraph of study material here...")


class LearningPathRequest(BaseModel):
    topic: str = Field(..., example="SQL")
