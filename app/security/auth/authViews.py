# authViews.py

import logging


from flask import request, jsonify, json
from flask_jwt_extended import decode_token
from flask.views import MethodView

from datetime import datetime, timezone

from app.utils import SchemaUtils

from app.security.token import TokenService
from app.security.auth import AuthService
from app.security.auth.shemas import UserLoginSchema


class LoginApi(MethodView):
    def __init__(self):
        self.token_service = TokenService()
        self.auth_service = AuthService()
        self.user_login_schema = UserLoginSchema()

    def post(self):
        """Método POST para login."""

        user_login_data = request.get_json()

        user = SchemaUtils.deserialize(
            UserLoginSchema(), user_login_data)

        # Autenticar o usuário
        user_auth = self.auth_service.authenticate_user(
            user.user_email, user.password
        )

        # Gerar o token para o usuário autenticado
        # O cliente pode usar uma biblioteca como 'jwt-decode' para ler o conteúdo do JWT,
        # como 'user_name', 'role_name' e a data de 'expiração'.
        # O cliente pode verificar se o token expirou e, se necessário, solicitar um novo login.
        # A assinatura do token, gerada com a chave privada do servidor, não pode ser decodificada pelo cliente,
        # mas pode ser verificada com a chave pública distribuida pelo servidor para garantir que o token é autêntico e não foi alterado.
        access_token = self.token_service.generate_token(
            user_auth.id, user_auth.user_email, user_auth.role.name)

        logging.info("0: LoginApi.post")

        # Decodificar o token para obter informações
        decoded_token = decode_token(access_token)
        exp_timestamp = decoded_token["exp"]
        iat_timestamp = decoded_token["iat"]

        # Converter timestamps para datas legíveis
        iat_date = datetime.fromtimestamp(iat_timestamp, tz=timezone.utc)
        exp_date = datetime.fromtimestamp(exp_timestamp, tz=timezone.utc)

        # Logar as datas
        logging.info("Token Issuance Date: %s", iat_date)
        logging.info("Token Expiration Date: %s", exp_date)

        # Retorna uma resposta com status 200 (OK) e corpo contendo o access_token.
        return jsonify(access_token), 200
