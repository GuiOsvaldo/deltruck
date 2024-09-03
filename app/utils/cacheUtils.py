# caheUtils.py

from datetime import timedelta
from flask import current_app


class CacheUtils:
    @staticmethod
    def get_cache_timeout_days():
        return current_app.config.get("CACHE_TIMEOUT_DAYS", 1)
