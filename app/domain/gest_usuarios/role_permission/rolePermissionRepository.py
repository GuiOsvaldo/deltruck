# rolePermissionRepository.py

from app.extensions import db

from app.utils import BaseRepository

from .rolePermission import RolePermission


class RolePermissionRepository(BaseRepository):
    def __init__(self):
        super().__init__(RolePermission)
