from pydantic import BaseModel, Field, EmailStr

class UserResponseDto(BaseModel):

    id: int = Field(
        description="User Id"
    )
    login: str = Field(
        min_length=3, 
        max_length=50,
        description="User Login"
    )
    contact_info: EmailStr = Field(
        min_length=5, 
        max_length=255,
        description="User Email"
    )