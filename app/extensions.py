# app/extensions.py

from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_caching import Cache
from flask_session import Session

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()
cache = Cache()


def init_extensions(app):
    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
