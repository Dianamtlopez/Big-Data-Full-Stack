# f-strings

class Estudiante:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    '''
    # Representacion informal de una cadena o de un objeto
    def __str__(self):
        # Usamos str para poder visualizar y ejecutar un resultado inmediatamente
        return f"Hola que tal, soy {self.nombre} {self.apellido}, tengo {self.edad} años."
    '''
    
    # Representacion oficial no ambigua y que se ejecuta con el código 
    def __repr__(self):
        # Tiene en cuenta el valor de las variables
        return f"Hola que tal, soy {self.nombre} {self.apellido}, tengo {self.edad} años."
        # Cuando creamos el objeto, este va a contener los valores como tal y no una cadena de sting
        
n = input("Ingrese su nombre: ")
a = input("Ingrese su apellido: ")
e = input("Ingrese su edad: ")

# Se crea el objeto
nuevo_estudiante = Estudiante(n, a, e)

# Se hace llamado a la funcion String
# print(f"{nuevo_estudiante}")

# Se hace llamado a la funcion String y al método rep
print(f"{nuevo_estudiante !r}")
