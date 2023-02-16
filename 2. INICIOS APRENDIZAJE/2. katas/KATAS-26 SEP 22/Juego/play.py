from enum import Enum

class Result(Enum):
    EQUAL = 0
    WINS = 1
    LOSES = 2

class Play(object):
    # Representa un ajugada
    def compare(self, otherPlay):
    # Se compara con la otra jugada y devuelve un Result de la comparación
        pass

class Paper(Play):
    def description(self):
        return 'Paper'
    
    def compare(self, otherPlay):
    # Compara papel con otras jugadas y devuelve un Result
        result = None
        if type(otherPlay) == Paper:
            result = Result.EQUAL
        elif type(otherPlay) == Scissors:
            result = Result.LOSES
        else:
            result = Result.WINS
        #Se compara con la otra jugada y devuelve un Result
        return result
    
class Sicssors(Play):
    def description(self):
        return 'Sicssors'
    
    def compare(self, otherPlay):
    # Compara papel con otras jugadas y devuelve un Result
        result = None
        if type(otherPlay) == Sicssors:
            result = Result.EQUAL
        elif type(otherPlay) == Rock:
            result = Result.LOSES
        else:
            result = Result.WINS
        #Se compara con la otra jugada y devuelve un Result
        return result

class Rock(Play):
    def description(self):
        return 'Rock'
    
    def compare(self, otherPlay):
    # Compara papel con otras jugadas y devuelve un Result
        result = None
        if type(otherPlay) == Rock:
            result = Result.EQUAL
        elif type(otherPlay) == Paper:
            result = Result.LOSES
        else:
            result = Result.WINS
        #Se compara con la otra jugada y devuelve un Result
        return result