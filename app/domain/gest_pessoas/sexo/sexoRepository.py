# sexoRepository.py

from app.extensions import db

from app.utils import BaseRepository

from .sexo import Sexo


class SexoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Sexo)
