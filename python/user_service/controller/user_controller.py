from fastapi import APIRouter, Depends
from fastapi import HTTPException
from user_service.service.user_service import UserService
from user_service.dto.user_request_dto import UserRequestDto
from common_lib_service.controller.base_controller import BaseController


class UserController(BaseController):
    def __init__(self):
        self.router = APIRouter()
        self._service = UserService()
        self._register_routes()

    def _register_routes(self):
        @self.router.get("/users")
        async def get_list():
            return self._service.get_list()
        
        @self.router.post("/users")
        async def create_user(data: UserRequestDto):
            try: 
                return self.success(self._service.create_user(data))
            except Exception as e:
                 return self.error(str(e), 400)