# rolePermission.py.py

from sqlalchemy import PrimaryKeyConstraint

from app.extensions import db


class RolePermission(db.Model):
    __tablename__ = "role_permission"
    __table_args__ = (
        PrimaryKeyConstraint("role_id", "permission_id"),
        {"schema": "deltruck"},
    )
    role_id = db.Column(db.Integer, db.ForeignKey("deltruck.role.id"))
    permission_id = db.Column(
        db.Integer, db.ForeignKey("deltruck.permission.id"))
