from user_service.entities.user import User
from sqlalchemy.orm import Session

class UserRepository:

    def get_user_by_login(self, login: str, session: Session):
        query = session.query(User)
        query.filter(User.login == login)
        return query.first()

    def save(self, user: User, session: Session) -> User:
        session.add(user)
        # TODO move commit from here make rollback transaction
        session.commit()
        session.refresh(user)
        return user
