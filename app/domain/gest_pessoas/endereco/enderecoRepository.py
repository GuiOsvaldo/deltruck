# enderecoRepository.py

from app.extensions import db

from app.utils import BaseRepository

from .endereco import Endereco


class EnderecoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Endereco)
