# sexoResponseSchema.py

from marshmallow import Schema, fields


class SexoResponseSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
