# endereco.py
from sqlalchemy.orm import relationship

from app.extensions import db


class Endereco(db.Model):
    __tablename__ = "endereco"
    __table_args__ = {"schema": "deltruck"}
    id = db.Column(db.Integer, primary_key=True)
    # Número da Residência, Rua, Avenida, Travessa, etc.
    linha_1 = db.Column(db.String)
    linha_2 = db.Column(
        db.String
    )  # Complemento, Apartamento, Edifício, Andar, Bloco, etc.
    bairro = db.Column(db.String)
    id_cidade = db.Column(db.Integer, db.ForeignKey("deltruck.cidade.id"))

    cidade = relationship("Cidade", lazy="joined")
