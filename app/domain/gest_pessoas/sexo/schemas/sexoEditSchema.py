# sexoEditSchema.py

from marshmallow import Schema, fields, post_load

from ..sexo import Sexo

class SexoEditSchema(Schema):
    id = fields.Int()
    nome = fields.Str()

    @post_load
    def make_user(self, data, **kwargs):
        return Sexo(**data)
