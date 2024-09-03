# authService.py

import logging


from app.utils import SingletonMeta

from app.domain.gest_usuarios.user import UserService
from app.security.securityConfig import SecurityConfig
from app.domain.gest_usuarios.user.exceptions import invalidPasswordException


class AuthService(metaclass=SingletonMeta):
    def __init__(self):
        self.user_service = UserService()

    def authenticate_user(self, user_email, password):
        """Autenticação baseada em user_email e password"""

        logging.info("0: AuthService.authenticate_user()")

        user = self.user_service.get_user_by_user_email(user_email)
        logging.info("1: AuthService.authenticate_user(): %s", user)

        # Verifica se a password fornecida corresponde à password criptografada.
        if not SecurityConfig.check_password(user.password, password):
            raise invalidPasswordException("Credenciais inválidas.")
        return user
