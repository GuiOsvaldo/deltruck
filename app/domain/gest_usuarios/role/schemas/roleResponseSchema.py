# roleResponseSchema.py

from marshmallow import Schema, fields


class RoleResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
