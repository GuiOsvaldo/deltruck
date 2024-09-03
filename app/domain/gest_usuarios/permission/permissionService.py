# permissionService.py

from app.utils import SingletonMeta

from .permission import Permission
from .permissionRepository import PermissionRepository


class PermissionService(metaclass=SingletonMeta):
    def __init__(self):
        self.permission_repository = PermissionRepository()
