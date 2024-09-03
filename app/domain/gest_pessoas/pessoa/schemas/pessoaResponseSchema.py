# pessoaResponseSchema.py

from marshmallow import Schema, fields

from app.domain.gest_pessoas.sexo import SexoResponseSchema
from app.domain.gest_pessoas.contacto import ContactoResponseSchema
from app.domain.gest_pessoas.endereco import EnderecoResponseSchema


class PessoaResponseSchema(Schema):
    id = fields.Int()
    primeiro_nome = fields.Str()
    ultimo_nome = fields.Str()
    num_identificacao = fields.Str()
    sexo = fields.Nested(SexoResponseSchema)
    contacto = fields.Nested(ContactoResponseSchema)
    endereco = fields.Nested(EnderecoResponseSchema)

