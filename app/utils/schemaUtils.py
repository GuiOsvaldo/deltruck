# schemaUtils.py

import logging

from marshmallow import Schema, ValidationError


class SchemaUtils:
    """Utilitários para serialização e desserialização usando marshmallow."""

    @staticmethod
    def serialize(schema: Schema, obj):
        """
        Serializa um objeto ou uma lista de objetos usando o esquema fornecido.

        Args:
        - schema (Schema): Instância do esquema de marshmallow usada para serialização.
        - obj: Objeto ou lista de objetos a ser serializado.

        Returns:
        - Dados serializados no formato JSON.
        """
        if isinstance(obj, list):
            return [schema.dump(item) for item in obj]
        return schema.dump(obj)

    @staticmethod
    def deserialize(schema: Schema, data):
        """
        Desserializa dados (por exemplo, JSON) usando o esquema fornecido.

        Args:
        - schema (Schema): Instância do esquema de marshmallow usada para desserialização.
        - data: Dados a serem desserializados.

        Returns:
        - dict: Dados desserializados como um dicionário.
        Raises:
        - ValidationError: Se os dados não forem válidos de acordo com o esquema.
        """
        try:
            return schema.load(data)
        except ValidationError as err:
            print(f"Erro de validação: {err.messages}")
            raise

    @staticmethod
    def deserialize_update(schema: Schema, data, instance, partial=False):
        """
        Atualiza uma instância existente usando o esquema fornecido e dados.

        Args:
        - schema (Schema): Instância do esquema de marshmallow usada para desserialização.
        - data: Dados a serem desserializados.
        - instance: Instância do objeto que será atualizada.
        - partial (bool, opcional): 
            - False: Requer que todos os campos estejam presentes no data para uma atualização completa (útil para requisições PUT).
            - True: Permite atualizações parciais, atualizando apenas os campos fornecidos no data (útil para requisições PATCH).

        Returns:
        - A instância do objeto atualizado.
        Raises:
        - ValidationError: Se os dados não forem válidos de acordo com o esquema.
        """
        try:
            loaded_data = schema.load(data, partial=partial)
            # Verifica se loaded_data é uma instância da mesma classe que a instância original
            if isinstance(loaded_data, instance.__class__):
                # Itera sobre os atributos da instância carregada
                for key, value in loaded_data.__dict__.items():
                    # Verifica se a instância original tem um atributo com o nome 'key'
                    if hasattr(instance, key):
                        # Atualiza o atributo da instância original com o valor da instância carregada
                        setattr(instance, key, value)
            
            return instance
        except ValidationError as err:
            print(f"Erro de validação: {err.messages}")
            raise
