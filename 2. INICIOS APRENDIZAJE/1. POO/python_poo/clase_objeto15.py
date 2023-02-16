# Clase y estático
import math

class Pastel:
    # Creacion del constructor y sus atributos
    def __init__(self, ingredientes, tamaño):
        self.ingredientes = ingredientes
        self.tamaño = tamaño
    # Como son multiples valores en un atrubito uso __repr__    
    def __repr__(self):
        return (f'Pastel({self.ingredientes}, 'f'{self.tapaño}) !r')
    
    def area(self):
        # método para hayar el area del pasetel solo con tamaño
        return self.tamaño_area(self.tamaño)
    
    @staticmethod
    # método independiente que aisla el tamaño de los ingredientes
    def tamaño_area(A):
        return A ** 2 * math.pi

# Valores ingresado en clase Pastely método tamaño_area     
nuevo_pastel = Pastel(['Harina', 'Azucar', 'Leche', 'Huevos', 'Crema'], 4)

print(nuevo_pastel.ingredientes)
print(nuevo_pastel.tamaño)
# Calculo realizado con el metodo statico y con valor independiente al ya ingresado
print(nuevo_pastel.tamaño_area(4))
        