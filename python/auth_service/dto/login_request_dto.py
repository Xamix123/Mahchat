from pydantic import BaseModel, Field


class LoginRequestDto(BaseModel):

    login: str = Field(min_length=3, max_length=50, description="User Login")
    password: str = Field(min_length=8, max_length=255, description="User password")
