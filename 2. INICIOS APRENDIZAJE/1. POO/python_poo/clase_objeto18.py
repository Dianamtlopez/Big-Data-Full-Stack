# Polimorfismo, método y herencia

# Polimorfismo por funcion
class Tomate:
    def tipo(self):
        print('Vegetal')
    def color(self):
        print('Rojo')
    
class Manzana:
    def tipo(self):
        print('Fruta')
    def color(self):
        print('Verde')

# Funciona como funcion ya que está de manera externa a la clase
# el método, se ubica dentro de la clase
def funcion(objeto):
    objeto.tipo()
    objeto.color()
    
nuevo_tomate = Tomate()
funcion(nuevo_tomate)
print('\n')
nueva_manzana = Manzana()
funcion(nueva_manzana)
print('\n')

# Polimorfismo con métodos, funciona bien cuando tenemo mas de dos clases

class Colombia:
    def capital(self):
        print('Santafé de Bogotá')
    
    def idioma(self):
        print('Españól')
        
class Francia:
    def capital(self):
        print('París')
    
    def idioma(self):
        print('Francés')

# Creación de los Objetos
nacionalidad = Colombia()
nacionalidad1 = Francia()

# Usado cuando existen varios objetos dentro del polimorfismo
for pais in (nacionalidad, nacionalidad1):
    pais.capital()
    pais.idioma()
    print('\n')

# Polimorfismo con herencia
# Igual metodo en todas las clases, con diferente funcion

class Aves:
    def volar(self):
        print('La mayoría de las aves pueden volar, pero algunas no!')

class Aguila(Aves):
    def volar(self):
        print('Las aguilas, pueden volar.')
        
class Gallina(Aves):
    def volar(self):
        print('Las gallinas, no pueden volar.')
        
# Objetos
obj_ave = Aves()
obj_aguila = Aguila()
obj_gallina = Gallina()

# Visualizacion del objeto
obj_ave.volar()
obj_aguila.volar()
obj_gallina.volar()
