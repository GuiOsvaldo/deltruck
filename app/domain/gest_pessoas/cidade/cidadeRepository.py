# cidadeRepository.py

from app.extensions import db

from app.utils import BaseRepository

from .cidade import Cidade


class CidadeRepository(BaseRepository):
    def __init__(self):
        super().__init__(Cidade)
