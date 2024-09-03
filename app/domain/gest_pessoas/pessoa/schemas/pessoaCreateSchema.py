# pessoaCreateSchema.py.py

from marshmallow import Schema, fields, post_load

from app.domain.gest_pessoas.contacto.schemas import ContactoCreateSchema
from app.domain.gest_pessoas.endereco.schemas import EnderecoCreateSchema

from app.domain.gest_pessoas.pessoa import Pessoa


class PessoaCreateSchema(Schema):
    primeiro_nome = fields.Str()
    ultimo_nome = fields.Str()
    num_identificacao = fields.Str()
    id_sexo = fields.Int()
    contacto = fields.Nested(ContactoCreateSchema)
    endereco = fields.Nested(EnderecoCreateSchema)

    @post_load
    def make_user(self, data, **kwargs):
        return Pessoa(**data)
