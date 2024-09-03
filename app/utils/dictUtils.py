# utils/dictUtils.py


class DictUtils:
    @staticmethod
    def get_key_by_value(dict, value):
        """
        Retorna a chave correspondictente ao valor especificadicto em um dicticionário.

        Args:
            dict (dictict): O dicticionário ondicte procurar.
            value (any): O valor para o qual encontrar a chave.

        Returns:
            any: A chave correspondictente ao valor, ou None se o valor não for encontradicto.
        """
        return next((key for key, val in dict.items() if val == value), None)
