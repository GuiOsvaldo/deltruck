# auth/__init__.py

from .authService import AuthService
from .authViews import *
from .shemas import *


def auth_blueprints(app, BASE_API_URL):
    login_view = LoginApi.as_view("login_api")

    app.add_url_rule(
        f"{BASE_API_URL}/auth/login",
        view_func=login_view,
        methods=["POST"],
    )
