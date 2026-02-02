from dotenv import load_dotenv
from common_lib_service.service.database import Database
from user_service.entity.user import User
from fastapi import HTTPException

class UserService:
    def __init__(self):
        self.db_session = Database().get_session()

    def get_list(self):
        self.db_session.query(User).all()

    def get_user(self, id):
        pass

    def create_user(self, data):
        pass


    def update_user(self, id, data):
        pass


    def delete_user(self, id):
        pass
