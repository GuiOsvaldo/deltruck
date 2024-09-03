# userLoginSchema.py

from marshmallow import Schema, fields, validate, post_load

from app.domain.gest_usuarios.user import User
from app.utils import ValidationUtils

class UserLoginSchema(Schema):
    user_email = fields.Str(
        required=True,
        validate=[ValidationUtils.email()],
    )
    password = fields.Str(
        required=True,
        validate=[ValidationUtils.password()],
    )

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
