# contactoCreateSchema.py

from marshmallow import Schema, fields


class ContactoCreateSchema(Schema):
    id = fields.Int()
    telefone_1 = fields.Str()
    telefone_2 = fields.Str()
