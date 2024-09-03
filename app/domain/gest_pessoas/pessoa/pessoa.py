# pessoa.py

from sqlalchemy.orm import relationship

from app.extensions import db


class Pessoa(db.Model):
    __tablename__ = "pessoa"
    __table_args__ = {"schema": "deltruck"}
    id = db.Column(db.Integer, primary_key=True)
    primeiro_nome = db.Column(db.String, nullable=False)
    ultimo_nome = db.Column(db.String, nullable=False)
    num_identificacao = db.Column(db.String, unique=True)
    id_sexo = db.Column(db.Integer, db.ForeignKey("deltruck.sexo.id"))
    id_contacto = db.Column(db.Integer, db.ForeignKey("deltruck.contacto.id"))
    id_endereco = db.Column(db.Integer, db.ForeignKey("deltruck.endereco.id"))

    sexo = relationship("Sexo", lazy="joined")
    contacto = relationship("Contacto", lazy="joined")
    endereco = relationship("Endereco", lazy="joined")

    def __repr__(self):
        return "id:{}, primeiro_nome:{}".format(self.id, self.primeiro_nome)
