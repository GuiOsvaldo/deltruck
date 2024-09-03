# domain/__init__.py
from .gest_usuarios import *
from .gest_pessoas import *
from .gest_encomendas import *


def register_domain_blueprints(app):
    BASE_API_URL = app.config["BASE_API_URL"]

    user_blueprints(app, BASE_API_URL)
