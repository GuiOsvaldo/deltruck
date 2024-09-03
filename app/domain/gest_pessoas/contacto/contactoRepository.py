# contactoRepository.py

from app.extensions import db

from app.utils import BaseRepository

from .contacto import Contacto


class ContactoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Contacto)
