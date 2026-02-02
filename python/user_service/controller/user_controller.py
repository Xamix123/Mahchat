from fastapi import APIRouter, Depends
from fastapi import HTTPException
from user_service.service.user_service import UserService

class UserController:
    def __init__(self):
        self.router = APIRouter()
        self._service = UserService()
        self._register_routes()

    def _register_routes(self):
        @self.router.get("/user")
        async def get_list():
            return self._service.get_list()
