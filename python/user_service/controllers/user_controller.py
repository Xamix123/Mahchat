from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from user_service.services.user_service import UserService
from user_service.dto.user_request_dto import UserRequestDto
from common_lib_service.controllers.base_controller import BaseController
from common_lib_service.services.database import Database


class UserController(BaseController):
    def __init__(self):
        self.router = APIRouter()
        self._service = UserService()
        self.db = Database()
        self._register_routes()

    def _register_routes(self):
        @self.router.get("/users")
        async def get_list():
            return self._service.get_list()

        @self.router.post("/users")
        async def create_user(
            data: UserRequestDto, session: Session = Depends(self.db.get_session)
        ):
            try:
                self.success(self._service.create_user(data, session))
            except Exception as e:
                return self.error(str(e), 400)
