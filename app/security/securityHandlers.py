# handlers/securityHandlers.py

import logging
import secrets

from flask import g, request, jsonify
from flask_jwt_extended import verify_jwt_in_request
from jwt.exceptions import InvalidTokenError


class SecurityHandlers:
    def __init__(self, app):
        self.app = app
        # self._register_before_requests()
        # self._register_after_requests()

    def _register_before_requests(self):
        """Registra o manipulador before_equest."""

        @self.app.before_request
        def generate_nonce():
            """Gera um nonce e o armazena no objeto `g` para uso posterior nas requisição."""
            g.csp_nonce = self._generate_nonce()
            nonce = getattr(g, "csp_nonce", None)
            logging.info(
                "SecurityHandlers._register_requests.generate_nonce(): %s", nonce)

        @self.app.before_request
        def required_jwt():
            """Verifica se um token JWT está presente e é válido para as requisições que exigem autenticação.
            """

            logging.info("0: before_request.required_jwt()")

            # Ignorar para o endpoint
            if request.path.endswith("/login"):
                return

            token = request.headers.get("Authorization")

            if not token:
                return (
                    jsonify(
                        {"message": "Missing Authorization Header: Token não fornecido"}
                    ),
                    401,
                )

            try:
                verify_jwt_in_request()
                logging.info("0: before_request.required_jwt() assinado")
                logging.info(
                    "1: before_request.required_jwt() usuário autenticado")

            except InvalidTokenError:
                return jsonify({"message": "Token inválido ou expirado"}), 401

    def _register_after_requests(self):
        """Registra o manipulador after_request."""

        @self.app.after_request
        def set_nonce(response):
            """
            Após cada requisição HTTP, este método:

            1. Obtém o nonce armazenado no objeto `g` (gerado anteriormente).
            2. Atualiza o cabeçalho `Content-Security-Policy` da resposta com o nonce gerado.

            É necessário que o front Obtem o nonce do cabeçalho `Content-Security-Policy` da resposta HTTP e  aplique a todos os elementos: '<style nonce={nonce}></style>' e `'<script nonce={nonce}></script>' inline para garantir que somente os scripts e estilos autorizados sejam executados.

            :param response: A resposta HTTP que será enviada ao cliente.
            :return: A resposta atualizada com o nonce no cabeçalho `Content-Security-Policy`.
            """
            nonce = getattr(g, "csp_nonce", None)

            logging.info("0: _register_requests.set_nonce(): %s", nonce)

            response.headers["Content-Security-Policy"] = response.headers.get(
                "Content-Security-Policy", ""
            ).replace("{nonce}", nonce)

            # Se o cliente tiver permissões de CORS apropriadas, ele pode acessar o cabeçalho da resposta e extrair o nonce.

            return response

    def _generate_nonce(self):
        """Gera um nonce aleatório de forma segura."""
        return secrets.token_urlsafe(
            16
        )  # Gera um nonce seguro com 16 bytes de segurança
