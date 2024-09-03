# cidadeService.py

from app.utils import SingletonMeta

from .cidade import Cidade
from .cidadeRepository import CidadeRepository


class CidadeService(metaclass=SingletonMeta):
    def __init__(self):
        self.cidade_repository = CidadeRepository()

    def get_all(self):
        return self.cidade_repository.find_all()
