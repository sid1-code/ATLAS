from sqlalchemy.orm import Session

from app.models.conversation import Conversation
from app.models.message import Message
from app.models.user import User
from app.schemas.chat import ChatRequest
from app.services.ai import AIService


class ConversationService:
    def __init__(self, ai_service: AIService | None = None):
        self.ai_service = ai_service or AIService()

    def ensure_user(self, db: Session, user_id: int) -> User:
        user = db.get(User, user_id)
        if user:
            return user
        user = User(id=user_id, email=f"local-{user_id}@atlas.local", display_name="Local user")
        db.add(user)
        db.flush()
        return user

    def create_conversation(self, db: Session, user_id: int, title: str) -> Conversation:
        self.ensure_user(db, user_id)
        conversation = Conversation(user_id=user_id, title=title)
        db.add(conversation)
        db.commit()
        db.refresh(conversation)
        return conversation

    def chat(self, db: Session, request: ChatRequest) -> tuple[Conversation, Message]:
        self.ensure_user(db, request.user_id)
        conversation = db.get(Conversation, request.conversation_id) if request.conversation_id else None
        if conversation is None:
            conversation = Conversation(user_id=request.user_id, title=request.message[:60])
            db.add(conversation)
            db.flush()
        if conversation.user_id != request.user_id:
            raise ValueError("Conversation does not belong to this user")
        db.add(Message(conversation_id=conversation.id, role="user", content=request.message))
        reply = Message(conversation_id=conversation.id, role="assistant", content=self.ai_service.generate_reply(request.message))
        db.add(reply)
        db.commit()
        db.refresh(conversation)
        db.refresh(reply)
        return conversation, reply


