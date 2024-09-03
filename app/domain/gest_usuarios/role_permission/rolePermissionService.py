# rolerolePermissionService.py

from app.utils import SingletonMeta

from .rolePermission import RolePermission
from .rolePermissionRepository import RolePermissionRepository


class RolePermissionService(metaclass=SingletonMeta):
    def __init__(self):
        self.rolePermission_repository = RolePermissionRepository()
