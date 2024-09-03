# pessoaRepository.py

from app.extensions import db

from app.utils import BaseRepository

from .pessoa import Pessoa


class PessoaRepository(BaseRepository):
    def __init__(self):
        super().__init__(Pessoa)
