# Herencia
# Clase Padre
class Pokemon:
    pass
    # Creacion del constructor
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        
    def descripcion(self):
        return '{}, es un pokemon de tipo: {}'.format(self.nombre, self.tipo)

# Clase hija    
class Pikachu(Pokemon):
    def ataque(self, tipo_ataque):
        return 'El pokemon Pikachu llamado {}, tiene el tipo de ataque: {}'.format(self.nombre, tipo_ataque)

# Clase hija
class Charmander(Pokemon):
    def ataque(self, tipo_ataque):
        return 'El pokemon Charmander llamado {}, tiene el tipo de ataque: {}'.format(self.nombre, tipo_ataque)

n = input('Ingrese el nombre del pokemon: ')
t = input('Ingrese el tipo del pokemon: ')
a = input('Ingrese el tipo de ataque del pokemon: ')

# creacion del objeto, haciendo llamado a la clae Pikachu
nuevo_pokemon = Pikachu(n, t)
# Visualizar el objeto nuevo_pokemon
print(nuevo_pokemon.descripcion())
# Visualizar ataque de la clase pikachu
print(nuevo_pokemon.ataque(a))

# creacion del objeto
nuevo_pokemon_1 = Charmander(n, t)
# Visualizar el objeto
print(nuevo_pokemon_1.descripcion())
# Visualizar ataque de la clase pikachu
print(nuevo_pokemon_1.ataque(a))


