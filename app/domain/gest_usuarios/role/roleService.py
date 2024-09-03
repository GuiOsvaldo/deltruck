# roleService.py.py

from app.utils import SingletonMeta

from .role import Role
from .roleRepository import RoleRepository


class RoleService(metaclass=SingletonMeta):
    def __init__(self):
        self.role_repository = RoleRepository()

    def get_all(self):
        return self.role_repository.find_all()
