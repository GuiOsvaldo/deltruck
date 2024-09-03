# user/__init__.py

from .user import User
from .userRepository import UserRepository
from .userService import UserService
from .userViews import *
from .schemas import *
from .exceptions import *


def user_blueprints(app, BASE_API_URL):
    users_views = UsersApi.as_view("users_api")
    # 'users_api' gera URLs para as rotas associadas à view function 'users_views'.
    # Exemplos:
    # - url_for('users_api') -> '{BASE_API_URL}/users'
    # - url_for('users_api', user_id=1) -> '{BASE_API_URL}/users/1'
    # - url_for('users_api', user_id=1, _method='edit') -> '{BASE_API_URL}/users/edit/1'

    app.add_url_rule(
        f"{BASE_API_URL}/users",
        view_func=users_views,
        methods=["GET", "POST"],
    )

    app.add_url_rule(
        f"{BASE_API_URL}/users/<int:user_id>",
        view_func=users_views,
        methods=["GET", "PUT", "PATCH", "DELETE"],
    )

    app.add_url_rule(
        f"{BASE_API_URL}/users/<int:user_id>/edit",
        view_func=users_views,
        methods=["GET"],
    )
