# security/__init__.py

from .securityConfig import SecurityConfig
from .securityHandlers import SecurityHandlers
from .auth import *
from .authz import *
from .token import *


def register_security_blueprints(app):
    BASE_API_URL = app.config["BASE_API_URL"]

    auth_blueprints(app, BASE_API_URL)
