from enum import Enum

class Affiliation(Enum):
    REBEL_ALLIANCE = 0
    GALACTIC_EMPIRE = 1
    UNKNOWN = 2
    
class StarWarsCharacter:
    # La clase Object esta implicita en la super clase y esta tiene todos los dunders
    def __init__(self, name, alias, affiliation):
        """
            Crea un personaje con nombre y alias
        """
        self.name = name
        self.alias = alias
        self.affiliation = affiliation
        
    def __repr__(self):
        """
            Muestra una representación textual del objeto
        """
        return f'<{self.__class__}: {self.name} {self.alias}>'
    
class ForceSensitive(StarWarsCharacter):
    """
        Representa personajes sensibles a la Fuerza
    """
    def __init__(self, name, alias, affiliation, midichlorians):
        super().__init__(name, alias, affiliation)
        self.midichlorians = midichlorians
        
    def unsheathe(self):
        """
            Este método, solo sirve para que mis subclases lo entiendan y no tenga que repetirlo
        """
        raise NotImplementedError()

class Jedi(ForceSensitive):
     # métodos de clase
    @classmethod # es un modificador
    def padawan(cls, name, alias):
      return cls(name, alias, 10)
    
    # métodos de clase
    @classmethod # es un modificador
    def master(cls, name, alias):
      """Crea un maestro jedi (con 100k midichlorianos)"""
      return cls(name, alias, 100000) # usa return

    # métodos de instancia y se inicia con el init
    def __init__(self, name, alias, midichlorians):
        super().__init__(name, alias, Affiliation.REBEL_ALLIANCE, midichlorians)
        # no usa return

    def unsheathe(self):
        return '▐▍░▐░░▣░▒░▒░▒▕|' + "█" * 40
    
class Sith(ForceSensitive):
    @classmethod
    def darkLord(cls, name, alias):
        return cls(name, alias, 120000)

    def __init__(self, name, alias, midichlorians):
        super().__init__(name, alias, Affiliation.GALACTIC_EMPIRE, midichlorians)
        
    def unsheathe(self):
        return '▔▔▔▔▔▔▔▔▔▝▔▔▔ ' + "█" * 40


chewie = StarWarsCharacter('Chewbacca', 'Chewie', Affiliation.REBEL_ALLIANCE)
print(chewie)
jabba = StarWarsCharacter('Jabba Dessilic Tiure', 'Jabba The Hutt', Affiliation.UNKNOWN)
print(jabba)

lista = [chewie, jabba]
print('\n',lista,'\n')

yoda = Jedi(alias = 'Master Yoda', name='Minch Yoda', midichlorians = 10000000)
print(yoda)

tupla = (yoda, chewie)
print('\n',tupla,'\n')

luke = Jedi('Luke Skywalker', 'Luke', 1000000)
print(luke)
palpatine = Sith('Palpatine', 'Darth Sidious', 1000000)
print(palpatine)
print(luke.unsheathe())
print(palpatine.unsheathe())
print(luke) # manda el mensaje __repr__ evalúa
yoda = Jedi.master('Minch Yoda','Master Yoda') # Método de clase para especializar la creación de instancias
print(yoda)

sith1 = Sith.darkLord("Anakin", "Darth Vader")
print(sith1)