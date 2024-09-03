# enderecoCreateSchema.py

from marshmallow import Schema, fields


class EnderecoCreateSchema(Schema):
    id = fields.Int()
    linha_1 = fields.Str()
    linha_2 = fields.Str()
    bairro = fields.Str()
    id_cidade = fields.Int()
