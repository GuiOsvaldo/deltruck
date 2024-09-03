# cidadeCache.py

import logging

from flask import current_app

from app.extensions import cache
from app.utils import CacheUtils, DateUtils

from datetime import timedelta

from .cidadeService import CidadeService


class CidadeCache:
    def __init__(self):
        self.cidade_service = CidadeService()

    def initialize_cidade_cache(self):
        """
        Inicializa o cache com dados de cidade.
        """
        try:
            cache_timeout_seconds = DateUtils.days_to_seconds(
                CacheUtils.get_cache_timeout_days())

            cidades = self.cidade_service.get_all()
            cidades_data = {cidade.id: cidade.nome for cidade in cidades}
            cache.set("cidades", cidades_data, timeout=cache_timeout_seconds)

        except Exception as e:
            logging.error(f"Erro ao inicializar o cache de cidades: {e}")

    @staticmethod
    def get_cidade_cache():
        """
        Retorna os dados do cache de cidade.
        """
        return cache.get("cidades")
