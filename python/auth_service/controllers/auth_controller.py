from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from auth_service.services.auth_service import AuthService
from auth_service.dto.login_request_dto import LoginRequestDto
from user_service.services.user_service import UserService
from common_lib_service.controllers.base_controller import BaseController
from common_lib_service.services.database import Database

class AuthController(BaseController):
    def __init__(self):
        self.router = APIRouter()
        self.db = Database()
        self._service = (
            self.get_auth_service()
        )  # need create separate folder in common_lib_service something like service manager
        self._register_routes()

    def _register_routes(self):
        @self.router.post("/login")
        async def login(
            data: LoginRequestDto, session: Session = Depends(self.db.get_session)
        ):
            try:
                return self.success(self._service.login(data, session))
            except Exception as e:
                return self.error(str(e), 400)

    def get_auth_service(self) -> "AuthService":
        return AuthService(UserService())
