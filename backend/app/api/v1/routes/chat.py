from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.conversation import ConversationService

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
def chat(payload: ChatRequest, db: Session = Depends(get_db)):
    try:
        conversation, reply = ConversationService().chat(db, payload)
    except ValueError as error:
        raise HTTPException(status_code=403, detail=str(error)) from error
    return ChatResponse(conversation_id=conversation.id, message=reply.content)


