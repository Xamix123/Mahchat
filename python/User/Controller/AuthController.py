from fastapi import FastAPI
from fastapi import HTTPException
from User.DTO.LoginRequest import LoginRequest
from User.DTO.RegistrationRequest import RegistrationRequest

app = FastAPI()

@app.post("/login")
async def login(data: LoginRequest):
    if data.checker is False:
        raise HTTPException(status_code=400, detail="Checker failed")

    return {
        "userId": 1,
        "userName": 'testName',
        "email": data.email,
        "token": 'test-token'
    }

@app.post("/registation")
async def registartion(data: RegistrationRequest):
    if data.checker is False:
        raise HTTPException(status_code=400, detail="Checker failed")
    result = {
        'status': 'success'
    }
    return result 