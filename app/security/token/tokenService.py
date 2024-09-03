# tokenService.py

import logging

from flask_jwt_extended import create_access_token

from app.exceptions import EntityUniqueViolationException


class TokenService:
    """Gerenciamento de tokens JWT"""

    def generate_token(self, user_id, user_name, role_name):
        """
        Gera um JWT (Token Web JSON) com o ID do usuário como parte do Payload (Carga Útil),
        usando a função `create_access_token` da biblioteca `flask_jwt_extended`.

        **Payload**: é a segunda parte do token e contém declarações de 'claims', como:
            - Claims Registradas: predefinidas como 'sub' (ID do usuário), 'exp' (data de expiração),'iat' (data de emissão) e 'jti' (JWT ID, um identificador único do token que é gerado automaticamente pela função 'create_access_token'), 'iss'(Issuer - Emissor),
            'aud' (Audience - Público) para quem o token é destinado.s
            - Claims Públicas: informações personalizadas que você pode definir, como o nome do usuário.
            - Claims Privadas: específicas para sua aplicação, definidas conforme suas necessidades.

        **Header (Cabeçalho)**: é a primeira parte do token, geralmente contém informações sobre o tipo de token
        e o algoritmo de assinatura utilizado para garantir a integridade do token.
            - Exemplo padrão: {"typ": "JWT", "alg": "HS256"}
        """

        # Definindo as informações personalizadas do token
        additional_claims = {
            "user_name": user_name,
            "role_name": role_name,
        }

        return create_access_token(
            identity=user_id, additional_claims=additional_claims
        )  # 'identity=user_id' Isto se torna o valor de 'sub' no token
