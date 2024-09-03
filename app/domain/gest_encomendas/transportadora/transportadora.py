# transportadora.py

from sqlalchemy.orm import relationship

from app.extensions import db


class Transportadora(db.Model):
    __tablename__ = "transportadora"
    __table_args__ = {"schema": "deltruck"}
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    id_contacto = db.Column(
        db.Integer, db.ForeignKey("deltruck.contacto.id"), nullable=False
    )
    id_endereco = db.Column(
        db.Integer, db.ForeignKey("deltruck.endereco.id"), nullable=False
    )

    contacto = relationship("Contacto", lazy="joined")
    endereco = relationship("Endereco", lazy="joined")
