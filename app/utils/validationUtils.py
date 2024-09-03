# utils/validationUtis.py

from marshmallow import validate, ValidationError

class ValidationUtils:
    @staticmethod
    def email():
        return validate.Email(
            error="O endereço de e-mail fornecido não é válido."
        )
    
    @staticmethod
    def password():
        return validate.Regexp(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@!#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/`~])[A-Za-z\d@!#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/`~]{8,}$",
            error=(
                "A senha deve ter pelo menos 8 caracteres, incluindo pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial."
            ),
        )