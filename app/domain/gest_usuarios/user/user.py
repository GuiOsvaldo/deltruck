# user.py


from sqlalchemy.orm import relationship

from app.extensions import db


class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {"schema": "deltruck"}
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    data_criacao = db.Column(
        db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp()
    )
    data_modificacao = db.Column(
        db.TIMESTAMP,
        server_default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )
    archived = db.Column(db.Boolean, nullable=False, default=False)
    profile_img_url = db.Column(db.String)
    id_role = db.Column(db.Integer, db.ForeignKey(
        "deltruck.role.id"), nullable=False)
    id_pessoa = db.Column(db.Integer, db.ForeignKey("deltruck.pessoa.id"))

    # Relacionamento N:1 com role
    # Atributo 'role' permite acessar à role associada a este usuário
    # 'back_populates' criar uma ligação bidirecional entre User e Role
    role = relationship("Role", lazy="joined", back_populates="users")

    pessoa = relationship("Pessoa", lazy="select")

    def __repr__(self):
        return (
            "id:{}, user_email:{}, data_modificacao:{}, pessoa: {}".format(
                self.id,
                self.user_email,
                self.data_modificacao,
                self.pessoa,
            )
        )

    # def serialize(self):
    #     """
    #     Converte objectos da classe em formato como 'JSON' ou 'XML'
    #     Return:
    #         dict: Um dicionário contendo os atributos do objeto.
    #     """
    #     return {
    #         "id": self.id,
    #         "username": self.username,
    #         "user_email": self.user_email,
    #         "data_criacao": self.data_criacao.isoformat(),
    #         "data_modificacao": self.data_modificacao.isoformat(),
    #         "role_name": self.role.name if self.role else None,
    #         "id_pessoa": self.id_pessoa,
    #     }
