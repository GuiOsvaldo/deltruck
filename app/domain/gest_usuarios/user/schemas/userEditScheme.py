# userEditScheme.py

from marshmallow import Schema, fields, post_load

from app.domain.gest_usuarios.user import User
from app.domain.gest_pessoas.pessoa.schemas import PessoaEditSchema
from app.utils import ValidationUtils

class UserEditScheme(Schema):
    """Esse schema pode ser usado tanto para:

     1. Response: Os dados retornados na resposta são utilizados em requisições PUT
     2. Request: Para valida e carregar os dado do cliente em requisições PUT
     """

    id = fields.Int(required=False)
    user_email = fields.Str(
        validate=[ValidationUtils.email()],
    )
    data_modificacao = fields.DateTime(format="%Y-%m-%d %H:%M:%S")
    archived = fields.Boolean()
    id_role = fields.Int()
    pessoa = fields.Nested(
        PessoaEditSchema, only=("id", "primeiro_nome", "ultimo_nome")
    )

    @post_load # Chamado no momento da desserializacao usando 'load'
    def make_user(self, data, **kwargs):
        return User(**data)

