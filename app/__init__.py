# app/__init__.py

import logging

from flask import Flask
from .extensions import init_extensions

from .config import AppConfigurator
from .domain import register_domain_blueprints
from .security import register_security_blueprints


def configure_logging():
    """Configura o logging para o aplicativo."""

    # Exibe mensagens de nível DEBUG e superiores(INFO,WARNING, ERROR e CRITICAL)
    logging.basicConfig(level=logging.DEBUG)

    # Reduz a verbosidade dos logs do watchdog
    logging.getLogger("watchdog.observers.inotify_buffer").setLevel(
        logging.WARNING)


def create_app(config_class):
    """Cria e configura a instância do aplicativo Flask."""

    configure_logging()

    app = Flask(__name__)

    # Carrega Configuração do app
    app.config.from_object(config_class)

    # Inicializar  extensões
    init_extensions(app)

    #  Configurar o app
    configurator = AppConfigurator(app)
    configurator.configure()

    # Importar o módulo domain e registra os blueprints
    from . import domain
    register_security_blueprints(app)
    register_domain_blueprints(app)

    if app.config.get('FLASK_ENV') != 'production':
        _show_log_configurations(app)

    return app


def _show_log_configurations(app):
    logging.info(
        "0:app/__init__._show_log_configurations():SQLALCHEMY_DATABASE_URI:  %s", app.config.get("SQLALCHEMY_DATABASE_URI")
    )
    logging.info(
        "1:app/__init__._show_log_configurations(): SQLALCHEMY_DATABASE_SCHEMA: %s", app.config.get("SQLALCHEMY_DATABASE_SCHEMA")
    )
    logging.info(
        "3:app/__init__._show_log_configurations(): SECRET_KEY: %s", app.config.get("SECRET_KEY")
    )

    logging.info(
        "4:app/__init__._show_log_configurations(): CACHE_DEFAULT_TIMEOUT: %s", app.config.get("CACHE_DEFAULT_TIMEOUT")
    )
