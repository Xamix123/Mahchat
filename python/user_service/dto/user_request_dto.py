from pydantic import BaseModel, Field, EmailStr


class UserRequestDto(BaseModel):

    login: str = Field(min_length=3, max_length=50, description="User Login")
    email: EmailStr = Field(min_length=5, max_length=255, description="User Email")
    password: str = Field(min_length=8, max_length=255, description="User password")
    password_confirmation: str = Field(
        min_length=8, max_length=255, description="User password confirmation"
    )
