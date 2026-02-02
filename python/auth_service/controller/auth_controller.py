from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

@app.post("/login")
async def login():

    return {
        "userId": 1,
        "userName": 'testName',
        "email": 'test',
        "token": 'test-token'
    }