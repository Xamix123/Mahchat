from common_lib_service.service.database import Database
from user_service.entity.user import User
from user_service.entity.contact_info import ContactInfo
from user_service.dto.user_request_dto import UserRequestDto
from user_service.dto.user_response_dto import UserResponseDto
from sqlalchemy.orm import Session
import bcrypt
import user_service.constants.contact_type as ContactTypeConstants


class UserService:
    def __init__(self):
        self.db = Database()

    def get_list(self):
        pass

    def get_user(self, id):
        pass

    def create_user(self, dto:UserRequestDto):
        session: Session = self.db.get_session()
        try:
            # hash password
            hashed_password = bcrypt.hashpw(
                dto.password.encode(),
                bcrypt.gensalt()
            ).decode()

            # create entity
            user = User(
                login=dto.login,
                password_hash=hashed_password,
                contact_info=ContactInfo(
                    contact_type_id=ContactTypeConstants.CONTACT_TYPE_EMAIL['id'],
                    value=dto.email
                )
            )

            # INSERT INTO DB
            session.add(user)

            # commit transaction
            session.commit()

            # refresh to get id
            session.refresh(user)

            return UserResponseDto(
                id=user.id,
                login=user.login,
                contact_info= "test@gmail.com"
            ) 
        finally:
            session.close()


    def update_user(self, id, data):
        pass


    def delete_user(self, id):
        pass
