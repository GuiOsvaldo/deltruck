# contactoEditSchema.py

from marshmallow import Schema, fields,post_load

from ..contacto import Contacto

class ContactoEditSchema(Schema):
    id = fields.Int()
    telefone_1 = fields.Str()
    telefone_2 = fields.Str()

    @post_load
    def make_user(self, data, **kwargs):
        return Contacto(**data)