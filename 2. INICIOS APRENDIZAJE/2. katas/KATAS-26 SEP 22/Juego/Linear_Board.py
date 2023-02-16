from Settings import BOARD_SIZE, VICTORY_STRIKE
from List_Utils import find_streak

# Tablero Lineal
class LinearBoard:
    """
        Representa un tablero de una sola columna
        x: representa al jugador 1
        o: representa al jugador 2
        None: repreenta un espacio vacío
    """

    @classmethod
    def fromList(cls, list):
        """Crea y devuelve un Linear Board a partir de una lista
           que representa una jugada
        """
        board = cls()
        # Se asigna a la variable privada _column la lista que se está recibiendo por argumentos
        board._colum = list
        # Se retorna la lista, la cual en este caso sería el tablero
        print(board)
        # return board

    def __init__(self):
        """
            Inicializar tablero vacío. o sea, lleno de None
        """
        # Columna vacía [None, None, None... tantas veces tenga BOARD_SIZE], en este caso 4
        self._column = [None] * BOARD_SIZE
        # print(self._column)

    # Verificar si el tablero está lleno
    def is_full(self):
        if self._column[-1] == None:
            return False
        else:
            return True

    def as_list(self):
        """Devuelve la representacion del tablero como una lista"""
        return self._column

    # Añadir fichas
    def add(self, char):
        """
            Añadir una ficha en dicha columna, en el primer espacio disponible
        """
        # Si no está lleno
        if not self.is_full():
            # Averiguo donde esta el primer None, lo cambio por un char
            i = self._column.index(None)
            # Lo cambio por un char
            self._column[i] = char

    def is_victory(self, char):
        """
            Verificar si es una victoria
        """
        # si ha logrado el objetivo que es hacer una linea de 3 elementos, devolver 
        # El tablero, el caracter que ganó y la cantidad de veces que está repetido
        return find_streak(self._column, char, VICTORY_STRIKE)

    # Si no es victoria
    def is_tie(self, char1, char2):
        """
            Verificar si es un
        """
        # Si no es victoria de nadie, hay empate
        if (self.is_victory(char1) == False) and (self.is_victory(char2) == False) and self.is_full():
            return True
        else:
            return False

tablero_lineal = LinearBoard()
tablero_lineal.add('x')
tablero_lineal.add('x')
tablero_lineal.add('x')
tablero_lineal.add('o')
print('Es una victoria: ',tablero_lineal.is_victory('x'))
print('Es una derrota:',tablero_lineal.is_tie('x','o'))
print('El tablero lineal es:',tablero_lineal.as_list())
print('El tablero está lleno: ',tablero_lineal.is_full())

