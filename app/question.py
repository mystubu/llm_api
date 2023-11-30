from pydantic import BaseModel

class Question(BaseModel):
    question: str
    chat_history: list
    