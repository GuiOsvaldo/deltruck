# cidadeEditSchema.py


from marshmallow import Schema, fields,post_load

from ..cidade import Cidade


class CidadeEditSchema(Schema):
    id = fields.Int()
    nome = fields.Str()

    @post_load
    def make_user(self, data, **kwargs):
        return Cidade(**data)


