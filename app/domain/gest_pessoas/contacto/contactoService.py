# contactoService.py

import logging

from app.utils import SingletonMeta

from .contacto import Contacto
from .contactoRepository import ContactoRepository


class ContactoService(metaclass=SingletonMeta):

    def __init__(self):
        self.contacto_repository = ContactoRepository()

    def create(self, contacto: Contacto):
        contacto_criado = self.contacto_repository.save(contacto)
        logging.info("1: ContactoService.create(): %s", contacto)
        return contacto_criado
