import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from user_service.controller.user_controller import UserController

app = FastAPI()

app.include_router(UserController().router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # frontend
        "http://127.0.0.1:8000",  # backend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)