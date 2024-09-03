# utils/baseRepository.py

import logging

from app.extensions import db
from .singletonMeta import SingletonMeta


class BaseRepository(metaclass=SingletonMeta):
    """Classe base para operações CRUD usando SQLAlchemy."""

    def __init__(self, model):
        self.model = model

    def save(self, entity):
        """
        Salva uma ou mais entidades no banco de dados.

        Args:
        - entities (list or db.Model): Entidade ou lista de entidades a serem salvas.

        Returns:
        - list or db.Model: A(s) entidade(s) salva(s).
        """
        if isinstance(entity, list):
            db.session.add_all(entity)
        else:
            db.session.add(entity)
        db.session.commit()
        return entity


    def find_all(self):
        """
        Recupera todas as entidades do modelo.

        Returns:
        - list: Lista de todas as entidades.
        """
        return db.session.query(self.model).all()

    def find_by_id(self, id: int):
        """
        Busca uma entidade pelo seu ID.

        Args:
        - id (int): O identificador da entidade.

        Returns:
        - db.Model: A entidade correspondente ao ID fornecido, ou None se não encontrada.
        """
        return db.session.get(self.model, id)

    def update(self, entity):
        """"""
        # Validate that the entity has a primary key before merging
        if not entity.id:
            raise ValueError("Entity must have a primary key value before updating.")

        return self._merge(entity)


    def _merge(self, entity):
        """"""
        db.session.merge(entity)
        db.session.commit()
        return entity
    
    @staticmethod
    def transactional(func):
        """Envolve a execução de uma função em uma transação.

            Args:
            - func (callable): A função a ser executada dentro da transação.

            Returns:
            - O resultado da função executada.

            Raises:
            - Exception: Lança a exceção capturada após rollback.
        """
        try:
            result = func()
            db.session.commit()
            return result
        except Exception as e:
            db.session.rollback()
            raise e
