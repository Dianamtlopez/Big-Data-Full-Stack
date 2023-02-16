from enum import Enum
class ColumnClassification(Enum):
    FULL = -1 # Peor opción: no se puede jugar
    MAYBE = 10 # puede ser. a saber como te va

class BaseOracle():
    def get_recommendation(self, board, player):
    """ Devuelve lista de recomendaciones (una por columna)"""
    pass