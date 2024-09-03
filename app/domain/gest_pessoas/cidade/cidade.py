# cidade.py

from app.extensions import db


class Cidade(db.Model):
    __tablename__ = "cidade"
    __table_args__ = {"schema": "deltruck"}
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
