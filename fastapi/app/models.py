from pydantic import BaseModel


class Prediction(BaseModel):
    question: str
    context: str
