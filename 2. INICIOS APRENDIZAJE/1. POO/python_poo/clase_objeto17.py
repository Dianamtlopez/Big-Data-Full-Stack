# Herencia y Polimorfismo
# Clase padre
class Animales:
    def __init__(self, nombre):
        #atributos
        self.nombre = nombre.upper()
        
    # Definir a los animales por el tipo
    def tipo_animal(self):
        pass
    
# Clase hija, como vamos a usar herencia, vamos a crear otra clase
class Leon(Animales):
    def tipo_animal(self):
        print(f'{self.nombre}, es un Animal Salvaje')

# Clase hija, como vamos a usar herencia, vamos a crear otra clase
class Perro(Animales):
    def tipo_animal(self):
        print(f'{self.nombre}, es un Animal Doméstico')

# Captura de datos
tipo = int(input('Seleccione el tipo de animal\n 1 León:\n 2 Perro: '))
n = input('Ingrese el nombre: ')

if tipo ==1: 
    # Creacion de Objetos
    nuevo_animal = Leon(n)

    # Llamado del objeto
    nuevo_animal.tipo_animal()
elif tipo == 2:
    # Creacion de Objetos
    nuevo_animal = Perro(n)

    # Llamado del objeto
    nuevo_animal.tipo_animal()
else:
    print(f'El tipo de animal {tipo}, no está definido')