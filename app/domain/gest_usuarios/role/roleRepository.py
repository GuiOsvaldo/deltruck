# roleRepository.py

from app.extensions import db

from app.utils import BaseRepository

from .role import Role


class RoleRepository(BaseRepository):
    def __init__(self):
        super().__init__(Role)
