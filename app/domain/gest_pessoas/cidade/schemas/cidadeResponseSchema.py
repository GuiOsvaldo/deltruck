# cidadeResponseSchema.py


from marshmallow import Schema, fields


class CidadeResponseSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
