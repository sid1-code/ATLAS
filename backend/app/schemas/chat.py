from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    conversation_id: int | None = Field(default=None, ge=1)
    user_id: int = Field(default=1, ge=1)
    message: str = Field(min_length=1, max_length=10000)


class ChatResponse(BaseModel):
    conversation_id: int
    message: str
    role: str = "assistant"


