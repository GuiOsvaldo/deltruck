# roleCache.py

import logging

from flask import current_app

from app.extensions import cache
from app.utils import CacheUtils, DateUtils

from .roleService import RoleService


class RoleCache:
    def __init__(self):
        self.role_service = RoleService()

    def initialize_role_cache(self):
        """
        Inicializa o cache com dados de papéis.
        """
        try:
            cache_timeout_seconds = DateUtils.days_to_seconds(
                CacheUtils.get_cache_timeout_days())

            roles = self.role_service.get_all()
            roles_data = {role.id: role.name for role in roles}
            cache.set("roles", roles_data, timeout=cache_timeout_seconds)

        except Exception as e:
            logging.error(f"Erro ao inicializar o cache de papéis: {e}")

    @staticmethod
    def get_role_cache():
        """
        Retorna os dados do cache de papéis.
        """
        return cache.get("roles")
