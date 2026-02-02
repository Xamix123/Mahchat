from pydantic import BaseModel
from typing import Optional

class RegistrationRequest(BaseModel):
    nickname: str
    email: str
    password: str
    checker: Optional[bool] = None