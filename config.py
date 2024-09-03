# config.py

import redis

from decouple import config


class Config(object):
    """Configurações comuns."""
    SQLALCHEMY_DATABASE_SCHEMA = config("DATABASE_SCHEMA")
    SECRET_KEY = config("SECRET_KEY")
    PORT = config("PORT", default=5000, cast=int)

    BASE_API_URL = config("BASE_API_URL")
    CORS_ORIGINS = config("CORS_ORIGINS")

    JWT_ACCESS_TOKEN_EXPIRES = config(
        "JWT_ACCESS_TOKEN_EXPIRES", default=900, cast=int)  # 15min
    # JWT_REFRESH_TOKEN_EXPIRES = config(
    #     "JWT_REFRESH_TOKEN_EXPIRES", default=86400, cast=int)  # 1dia
    # JWT_SECRET_KEY = config("JWT_SECRET_KEY")
    JWT_PRIVATE_KEY = config("JWT_PRIVATE_KEY")  # Chave Privada JWT
    JWT_PUBLIC_KEY = config("JWT_PUBLIC_KEY")  # Chave Pública JWT

    # Configura Flask-Caching para usar Redis
    CACHE_TYPE = "redis"
    CACHE_DEFAULT_TIMEOUT = config(
        "CACHE_DEFAULT_TIMEOUT", default=600, cast=int)
    # Definindo o timeout do cache em horas (por exemplo, 24 horas)
    CACHE_TIMEOUT_DAYS = config("CACHE_TIMEOUT_DAYS", default=1, cast=int)
    REDIS_CLIENT = redis.Redis(
        host=config("REDIS_HOST", default="localhost"),
        port=int(config("REDIS_PORT", default=6379)),
        db=int(config("REDIS_DB", default=0)),
        password=config("REDIS_PASSWORD", default=None),
    )
    CACHE_REDIS = REDIS_CLIENT


class DevConfig(Config):
    """Configurações de desenvolvimento local, para testes rápidos."""
    FLASK_ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = config("DATABASE_URI_LOCAL_DEV")


class TestConfig(Config):
    """Configurações de teste local, para testes mais abragentes."""
    FLASK_ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = config("DATABASE_URI_LOCAL_TEST")


class StagingConfig(Config):
    """Configurações de staing , semelhante ao de produção(pré-produção)."""
    FLASK_ENV = "staging"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = config("DATABASE_URI_REMOTE_STAGING")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    """Configurações de produção."""
    FLASK_ENV = "production"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = config("DATABASE_URI_REMOTE_PROD")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def get_config():
    env = config('FLASK_ENV', default='development')
    if env == 'testing':
        return 'config.TestConfig'
    elif env == 'staging':
        return 'config.StagingConfig'
    elif env == 'production':
        return 'config.ProdConfig'
    else:
        return 'config.DevConfig'
