from common_lib_service.services.database import Database
from sqlalchemy.orm import Session
from user_service.entities.user import User
from auth_service.dto.login_request_dto import LoginRequestDto
from user_service.services.user_service import UserService
from common_lib_service.services.password_checker import PasswordHasher


class AuthService:
    def __init__(self, user_service: UserService):
        self.db = Database()
        self.pasword_checker = PasswordHasher()
        self.user_service = user_service

    def login(
            self, 
            dto:LoginRequestDto,
            session: Session
        )-> bool:
        user = self.user_service.get_user_by_login(
            dto.login,
            session
        )

        return self.check_password(user, dto.password)

    def check_password(self, user: User, password: str) -> bool:
        return self.pasword_checker.verify(password, user.password_hash)