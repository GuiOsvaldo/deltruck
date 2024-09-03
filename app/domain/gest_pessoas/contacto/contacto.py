# contacto.py

from app.extensions import db


class Contacto(db.Model):
    __tablename__ = "contacto"
    __table_args__ = {"schema": "deltruck"}
    id = db.Column(db.Integer, primary_key=True)
    telefone_1 = db.Column(db.Integer)
    telefone_2 = db.Column(db.Integer)
