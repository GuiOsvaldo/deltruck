# permissionRepository.py

from app.extensions import db

from app.utils import BaseRepository

from .permission import Permission


class PermissionRepository(BaseRepository):
    def __init__(self):
        super().__init__(Permission)
