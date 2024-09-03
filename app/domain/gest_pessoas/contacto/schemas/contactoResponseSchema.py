# contactoResponseSchema.py

from marshmallow import Schema, fields


class ContactoResponseSchema(Schema):
    id = fields.Int()
    telefone_1 = fields.Str()
    telefone_2 = fields.Str()
