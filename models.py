from pydantic import BaseModel

class LogModel(BaseModel):
    service: str
    level: str
    message: str
