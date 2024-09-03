# sexoCache.py

import logging

from flask import current_app

from app.extensions import cache
from app.utils import CacheUtils, DateUtils

from datetime import timedelta

from .sexoService import SexoService


class SexoCache:
    def __init__(self):
        self.sexo_service = SexoService()

    def initialize_sexo_cache(self):
        """
        Inicializa o cache com dados de sexo.
        """
        try:
            cache_timeout_seconds = DateUtils.days_to_seconds(
                CacheUtils.get_cache_timeout_days())

            sexos = self.sexo_service.get_all()
            sexos_data = {sexo.id: sexo.nome for sexo in sexos}
            cache.set("sexos", sexos_data, timeout=cache_timeout_seconds)

        except Exception as e:
            logging.error(f"Erro ao inicializar o cache de sexos: {e}")

    @staticmethod
    def get_sexo_cache():
        """
        Retorna os dados do cache de sexo.
        """
        return cache.get("sexos")
