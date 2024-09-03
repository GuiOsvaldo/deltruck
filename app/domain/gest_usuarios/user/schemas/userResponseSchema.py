# userResponseSchema.py

from marshmallow import Schema, fields, post_dump

from app.domain.gest_usuarios.role.schemas import RoleResponseSchema
from app.domain.gest_pessoas.pessoa.schemas import PessoaResponseSchema


class UserResponseSchema(Schema):
    id = fields.Int()
    user_email = fields.Str()
    data_criacao = fields.DateTime(format="%Y-%m-%d %H:%M:%S")
    data_modificacao = fields.DateTime(format="%Y-%m-%d %H:%M:%S")
    role = fields.Nested(RoleResponseSchema, only=[
        "name"
    ])
    archived = fields.Bool()
    pessoa = fields.Nested(PessoaResponseSchema, only=(
        "primeiro_nome", "ultimo_nome"))

    @post_dump
    def add_fields(self, data, **kwargs):
        """Extrai campos do objeto aninhado e adiciona diretamente à resposta."""
        pessoa = data.get('pessoa', {})
        role = data.get('role', {})
        data['primeiro_nome'] = pessoa.get('primeiro_nome')
        data['ultimo_nome'] = pessoa.get('ultimo_nome')
        data['role_name'] = role.get('name')
        # Remove os campos aninhados se não forem mais necessários
        data.pop('pessoa', None)
        data.pop('role', None)
        return data
