# userRepository.py

from app.extensions import db

from app.utils import BaseRepository

from .user import User
from ..role import Role


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    def find_user_by_user_email(self, user_email):
        return db.session.query(User).filter_by(user_email=user_email).one_or_none()

    def find_all_except_role_user_and_root(self):
        """Retorna todos os usuários, exceto aqueles com os papéis 'USER' e 'ROOT'."""
        return (
            db.session.query(User)
            .join(User.role)
            .filter(Role.name.notin_(["USER", "ROOT"]))
            .all()
        )
