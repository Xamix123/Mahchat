import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from user_service.controllers.user_controller import UserController
from auth_service.controllers.auth_controller import AuthController
from common_lib_service.services.expection_handler import ExceptionHandler

app = FastAPI()

app.include_router(UserController().router)
app.include_router(AuthController().router)

ExceptionHandler.register(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
