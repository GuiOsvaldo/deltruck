# userViews.py

import logging

from flask import request, jsonify, json

from app.utils import BaseProtectedView, SchemaUtils, SchemaUtils, HateoasLinkGenerator

from app.domain.gest_usuarios.user import UserService
from app.domain.gest_usuarios.user.schemas import UserCreateSchema, UserResponseSchema, UserEditScheme

from app.domain.gest_pessoas.pessoa import PessoaService
from app.domain.gest_pessoas.pessoa.schemas import PessoaCreateSchema

class UsersApi(BaseProtectedView):
    def __init__(self):
        super().__init__()
        self.user_service = UserService()
        self.pessoa_service = PessoaService()
        self.hateos_link_generator = HateoasLinkGenerator(
            {
                "self": "users_api",
            }
        )

    def post(self):
        user_data = request.get_json()
        pessoa_data = user_data.pop('pessoa', None)

        pessoa = SchemaUtils.deserialize(
            PessoaCreateSchema(), pessoa_data)

        user = SchemaUtils.deserialize(UserCreateSchema(), user_data)

        # Associa a instância de Pessoa ao usuário
        # user.pessoa = pessoa

        # Cria o usuário no banco de dados, junto com a nova pessoa associada
        # user_criado = self.user_service.create(user)

        logging.debug("0: UsersApi.post")

        pessoa_criado = self.pessoa_service.create_pessoa_with_initial_details(
            pessoa)

        user.pessoa = pessoa_criado

        user_criado = self.user_service.create(user)

        logging.info("1: UsersApi.post")

        # retorna uma resposta com status 201 (CREATED) e corpo contendo os dados do usuário.
        return jsonify(SchemaUtils.serialize(
            UserResponseSchema(), user_criado)), 201

    def get(self, user_id=None):
        if user_id is None:
            return self._get_all()
        elif not request.path.endswith("/edit"):
            return self._get_user(user_id)
        return self._get_user_edit(user_id)

    def _get_all(self):
        """ """
        users = self.user_service.get_all_except_role_user_and_root()
        # Retorna uma resposta com status 200 (OK) e corpo contendo a lista de usuários
        return jsonify(SchemaUtils.serialize(UserResponseSchema(), users)), 200

    def _get_user(self, user_id):
        """ """
        user = self.user_service.get_by_id(user_id)

        # Retorna uma resposta com status 200 (OK) e corpo contendo o usuário.
        return jsonify(SchemaUtils.serialize(UserResponseSchema(), user)), 200

    def _get_user_edit(self, user_id):
        """ """
        user = self.user_service.get_by_id(user_id)

        # Retorna uma resposta com status 200 (OK) e corpo contendo o usuário.
        return jsonify(SchemaUtils.serialize(UserEditScheme(), user)), 200

    def put(self, user_id):
        """
        Atualiza um recurso existente com todos os campos fornecidos.

        Recomendações para o uso do método PUT:
            - Inclua todos os campos do recurso, mesmo aqueles que não serão modificados.
            - Use valores mascarados para campos sensíveis que não devem ser alterados.
        """

        user_data = request.get_json()
        
        user = self.user_service.get_by_id(user_id)

        user_actualizado = SchemaUtils.deserialize_update(
            UserEditScheme(), user_data, user)

        logging.info("0: UsersApi.PUT: %s ", user_actualizado)
        logging.info("1: UsersApi.PUT: %s ", user_actualizado.pessoa)

        # Actualiza o usuário no banco de dados, junto com a nova pessoa associada
        #self.user_service.update(user_actualizado)

        # gera a resposta HATEOAS.
        hateoas_response_data = self.hateos_link_generator.generate_response(user_id)

        # Retorna uma resposta com status 200 (OK) e corpo contendo os links HATEOAS.
        return jsonify(hateoas_response_data), 200

    def patch(self, user_id):
        pass
