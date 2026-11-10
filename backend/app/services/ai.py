class AIService:
    """Provider-neutral boundary for future model integrations."""

    def generate_reply(self, message: str) -> str:
        return f"ATLAS is connected. I received: {message}"


