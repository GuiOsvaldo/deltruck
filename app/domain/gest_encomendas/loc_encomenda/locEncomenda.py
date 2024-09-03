# locEncomenda.py

from sqlalchemy.orm import relationship

from app.extensions import db


class LocEncomenda(db.Model):
    __tablename__ = "loc_encomenda"
    __table_args__ = {"schema": "deltruck"}
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    data_localizacao_encomenda = db.Column(
        db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp()
    )
    id_encomenda = db.Column(
        db.Integer, db.ForeignKey("deltruck.encomenda.id"), nullable=False
    )

    # Relacionamento com Encomenda
    # Parte-1 do relacionamento bidirecional com Encomenda
    # Isso permite acessar a encomenda associada a esta localização.
    encomenda = relationship(
        "Encomenda", lazy="joined", back_populates="locs_encomenda"
    )
