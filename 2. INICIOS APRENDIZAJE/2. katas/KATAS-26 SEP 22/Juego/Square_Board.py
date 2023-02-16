from Linear_Board import LinearBoard
from Settings import BOARD_SIZE, VICTORY_STRIKE
from List_Utils import *


class SquareBoard():
    """
        Clase que representa un tablero Cuadrado
        métodos mara:
        1. Añadir un carácter (jugar en una columna)
        2. Detectar la victoria de un jugador
        3. Detectar el empate de 2 jugadores
        4. Detectar que el tablero está lleno
         
    """
    # Añadir un __repr__

    @classmethod
    def from_list(cls, list_of_list):
        """Transforma una lista de lista en una lista de LinearBoards"""
        colums = []
        for element in list_of_list:
            colums.append(LinearBoard.fromList(element))
        board = cls()
        board._columns = colums
        return board

    def __init__(self):
        """
            Inicializa 4 el tableros vacíos. usease, lleno de None
        """
        self._columns = [LinearBoard() for i in range(BOARD_SIZE)]
    
    def __repr__(self):
        """Devuelve una representacion textual del objeto"""
        # obtengo la representacion como matriz
        matrix = self.as_matrix()
        # le quito los none y los sustituyo po '-'
        matrix = replace_matrix(matrix, lambda x: x == None, '-')
        # transpongo esa matriz
        transp = transpose(matrix)
        # na invierto
        transp.reverse()
        # genero una cadena con todas estas listas
        tmp = '\n'
        for row in transp:
            for element in row:
                tmp = tmp + '\n' + elemento
            tmp = tmp + '\n'
        return f'<{self.__class__}: {tmp}>'
        
    def is_full(self):
        """
            Devuelve True si el tablero está lleno
        """
        all_full = True
        for board in self._columns:
            all_full = all_full and board.is_full()
        return all_full

    def is_victory(self, char):
        # empiezo a trabajar con la primera victoria por columna hecha
        return self._any_vertical_victory(char) or self._any_horizontal_victory(char) or self._any_rising_victory(char) or self._any_sinking_victory(char)

    def add(self, char, index):
        """
            Añade una 'ficha' en el primer espacio disponible de cada columna
        """
        self._columns[index].add(char)       
    
    def as_matrix(self):
        """ Ddevuelve su representacion como matriz"""
        matrix = []
        for LinearBoard in self._columns:
            matrix.append(LinearBoard.as_list())
        return matrix

    def _any_vertical_victory(self, char):
        # Valor inofensivo
        victory = False
        for LinearBoard in self._columns:
            victory = victory or LinearBoard.is_victory(char)
        return victory

    def _any_horizontal_victory(self, char):
        """Averigua si en el tablero hay una victoria horizontal, rotando el tablero, y al 
        tablero resultante preguntandole si tiene una victoria vertical"""
        # obtengo la matriz que representa al tablero actual (self)
        matrix = self.as_matrix()
        # transpongo esa matriz
        transp = transpose(matrix)
        # creo un tablero temporal a partir de esa matriz
        tmp = SquareBoard.from_list(transp)
        # le pregunto si tiene alguna victoria vertical
        result = tmp._any_vertical_victory(char)
        # devuelvo ese valor
        return result

    def _any_rising_victory(self, char):
        # obtengo la representación matricial
        matrix = self.as_matrix()
        #invierto la matriz
        matrix = reverse_matrix(matrix)
        # si había victoria ascendente en la orginal, en
        # la invertida, la tengo descendente
        # creo un tablero temporal con la invertida
        tmp = SquareBoard.from_list(matrix)
        #miro si hay victoria descendente
        return tmp._any_sinking_victory(char)
    
    def _any_sinking_victory(self, char):
        # obtengo la representacion matricial del tablero
        matrix = self.as_matrix()
        # le meto displace matrix en todo
        matrix = displace_matrix(matrix)
        # si había victoria descendente, ahora es horizontal
        # creo un tablero temporal con esa matriz desplazada
        # si hay una victoria horizontal en la desplazada,en la
        # original, habia una decendente
        tmp = SquareBoard.from_list(matrix)
        return tmp._any_horizontal_victory(char)

tablero_cuadrado = SquareBoard()
print(tablero_cuadrado)
tablero_cuadrado.add('x', 0)
tablero_cuadrado.add('x', 1)
tablero_cuadrado.add('x', 2)
tablero_cuadrado.add('o', 3)
tablero_cuadrado.add('x', 0)
tablero_cuadrado.add('x', 1)
tablero_cuadrado.add('x', 2)
tablero_cuadrado.add('o', 3)
tablero_cuadrado.add('x', 0)
tablero_cuadrado.add('x', 1)
tablero_cuadrado.add('x', 2)
tablero_cuadrado.add('o', 3)
tablero_cuadrado.add('x', 0)
tablero_cuadrado.add('x', 1)
tablero_cuadrado.add('x', 2)
tablero_cuadrado.add('o', 3)
print('Es una victoria: ',tablero_cuadrado.is_victory('x'))
print('La matriz lineal es:',tablero_cuadrado.as_matrix())
print('La matriz está llena: ',tablero_cuadrado.is_full())
print('Es una victoria vertical: ',tablero_cuadrado._any_vertical_victory('x'))
# print('Es una victoria horizontal: ',tablero_cuadrado._any_horizontal_victory('x'))
# print('Es una victoria en algun lugar: ',tablero_cuadrado._any_sinking_victory('x'))
