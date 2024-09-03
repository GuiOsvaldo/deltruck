# authz/authorization.py

from functools import wraps

from werkzeug.exceptions import Forbidden


class Authorization:
    def role_required(self, *required_roles):
        """Decorador que garante que o usuário possui um dos papéis necessários para acessar uma rota.

        Args:
        - required_roles (tuple): Papéis necessários para acessar a rota.

        Returns:
        - function: A função decorada que verifica a autorização do usuário.
        """
        def decorator(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                # 88888888
                raise Forbidden(
                    description="Você não possui os papéis necessários para acessar este recurso.")
                # Continuar com a execução da rota
                return f(*args, **kwargs)

            return wrapper

        return decorator
