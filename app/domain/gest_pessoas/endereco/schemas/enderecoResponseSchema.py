# enderecoResponseSchema.py

from marshmallow import Schema, fields

from app.domain.gest_pessoas.cidade.schemas import CidadeResponseSchema


class EnderecoResponseSchema(Schema):

    id = fields.Int()
    linha_1 = fields.Str()
    linha_2 = fields.Str()
    bairro = fields.Str()
    cidade = fields.Nested(CidadeResponseSchema)
