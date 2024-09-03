# sexo.py

from app.extensions import db


class Sexo(db.Model):
    __tablename__ = "sexo"
    __table_args__ = {"schema": "deltruck"}
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return "id:{}, nome:{}".format(self.id, self.nome)
