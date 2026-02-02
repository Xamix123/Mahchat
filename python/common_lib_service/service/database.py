import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_SERVER = os.getenv("DB_SERVER")
DB_NAME = os.getenv("DB_NAME")
DB_DRIVER = os.getenv("DB_DRIVER") 

class Database:
    def __init__(self):
        self.session_maker = self._make_session()

    def _make_connection(self):
        connection_string = (
            f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"
            f"?driver={DB_DRIVER}&Encrypt=yes&TrustServerCertificate=yes"
        )
        return create_engine(connection_string)

    def _make_session(self):
        return sessionmaker(bind=self._make_connection())()

    def get_session(self):
        return self.session_maker