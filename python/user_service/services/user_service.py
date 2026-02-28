from common_lib_service.services.database import Database
from user_service.entities.user import User
from user_service.entities.contact_info import ContactInfo
from user_service.dto.user_request_dto import UserRequestDto
from user_service.dto.user_response_dto import UserResponseDto
from sqlalchemy.orm import Session
import bcrypt
import user_service.constants.contact_type as ContactTypeConstants
from user_service.repository.user_repository import UserRepository
from user_service.exceptions.user_does_not_exists_exception import (
    UserDoesNotExistException,
)
from common_lib_service.services.password_checker import PasswordHasher


class UserService:
    def __init__(self):
        self.db = Database()
        self.user_repository = UserRepository()
        self.password_hasher = (
            PasswordHasher()
        )  # don`t use new move to separate service

    def get_list(self):
        pass

    def get_user(self, id):
        pass

    def get_user_by_login(self, login: str, session: Session) -> User:
        user = self.user_repository.get_user_by_login(login, session)

        if user == None:
            raise UserDoesNotExistException(login)

        return user

    def create_user(self, dto: UserRequestDto, session: Session) -> UserResponseDto:
        try:  # TODO move from here
            # hash password
            hashed_password = self.password_hasher.hash(dto.password)

            # create entity
            user = User(
                login=dto.login,
                password_hash=hashed_password,
                contact_info=ContactInfo(
                    contact_type_id=ContactTypeConstants.CONTACT_TYPE_EMAIL["id"],
                    value=dto.email,
                ),
            )

            user = self.user_repository.save(user, session)
            return UserResponseDto(
                id=user.id, login=user.login, contact_info=user.contact_info.value
            )
        finally:
            # TODO move from here
            session.close()

    def update_user(self, id, data):
        pass

    def delete_user(self, id):
        pass
