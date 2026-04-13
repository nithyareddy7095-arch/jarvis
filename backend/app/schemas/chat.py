from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    farmer_id: int | None = None
    question: str = Field(..., min_length=2)
    language: str = "en"


class ChatResponse(BaseModel):
    answer: str
    tips: list[str]
    stage: str
