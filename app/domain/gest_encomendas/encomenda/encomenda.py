# encomenda.py

from sqlalchemy.orm import relationship

from app.extensions import db


class Encomenda(db.Model):
    __tablename__ = "encomenda"
    __table_args__ = {"schema": "deltruck"}
    id = db.Column(db.Integer, primary_key=True)
    data_encomenda = db.Column(
        db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp()
    )
    id_pessoa_cliente_final = db.Column(
        db.Integer, db.ForeignKey("deltruck.pessoa.id"), nullable=False
    )
    id_transportadora = db.Column(
        db.Integer, db.ForeignKey("deltruck.transportadora.id"), nullable=False
    )

    pessoa_cliente_final = relationship("Pessoa", lazy="joined")
    transportadora = relationship("Transportadora", lazy="joined")

    # Relacionamento com LocEncomenda
    # Parte-2 do relacionamento bidirecional com LocEncomenda
    # Isso permite acessar todas as localizações associadas a esta encomenda.
    locs_encomenda = relationship(
        "LocEncomenda", back_populates="encomenda", lazy="select"
    )
