# pessoaEditSchema.py

from marshmallow import Schema, fields, post_load

from app.domain.gest_pessoas.sexo import SexoEditSchema
from app.domain.gest_pessoas.contacto import ContactoEditSchema
from app.domain.gest_pessoas.endereco import EnderecoEditSchema
from ..pessoa import Pessoa


class PessoaEditSchema(Schema):
    id = fields.Int()
    primeiro_nome = fields.Str()
    ultimo_nome = fields.Str()
    num_identificacao = fields.Str()
    sexo = fields.Nested(SexoEditSchema)
    contacto = fields.Nested(ContactoEditSchema)
    endereco = fields.Nested(EnderecoEditSchema)

    @post_load
    def make_user(self, data, **kwargs):
        return Pessoa(**data)


