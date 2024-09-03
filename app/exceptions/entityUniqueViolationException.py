# exceptions/entityUniqueViolationException.py


class EntityUniqueViolationException(Exception):
    def __init__(self, message):
        super().__init__(message)
