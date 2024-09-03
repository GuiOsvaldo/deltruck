# enderecoService.py

import logging

from app.utils import SingletonMeta

from .endereco import Endereco
from .enderecoRepository import EnderecoRepository


class EnderecoService(metaclass=SingletonMeta):
    def __init__(self):
        self.endereco_repository = EnderecoRepository()

    def create(self, endereco: Endereco):
        endereco_criado = self.endereco_repository.save(endereco)
        logging.info("1: EnderecoService.create(): %s", endereco)
        return endereco_criado
