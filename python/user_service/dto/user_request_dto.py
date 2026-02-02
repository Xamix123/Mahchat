from pydantic import BaseModel

class UserRequestDTO(BaseModel):
    nickname: str
    email: str
    password: str