# permission.py

from sqlalchemy.orm import relationship

from app.extensions import db


class Permission(db.Model):
    __tablename__ = "permission"
    __table_args__ = {"schema": "deltruck"}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String, nullable=False, unique=True
    )  # ex., 'create', 'edit', 'view', 'archive'

    # Relacionamento 1:N com role(atraveis da role_permission)
    # O atributo 'roles' permite acessar todos as roles associados a esta permissao
    # 'back_populates' criar uma ligação bidirecional entre Role e Permission
    roles = relationship(
        "Role",
        secondary="deltruck.role_permission",
        back_populates="permissions",
        lazy="select",
    )

    def __repr__(self):
        return "id:{}, name:{}".format(self.id, self.name)
