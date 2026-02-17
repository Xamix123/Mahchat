import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


DB_USER = os.environ["POSTGRES_USER"]
DB_PASSWORD = os.environ["POSTGRES_PASSWORD"]
DB_NAME = os.environ["POSTGRES_DB"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]


class Database:
    def __init__(self):
        self.engine = self._create_engine()
        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False
        )

    def _create_engine(self):
        connection_string = (
            f"postgresql+psycopg2://"
            f"{DB_USER}:{DB_PASSWORD}"
            f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )

        print("Connection:", connection_string)

        return create_engine(connection_string, echo=True)

    def get_session(self) -> Session:
        return self.SessionLocal()