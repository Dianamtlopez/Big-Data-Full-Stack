# Método contructor

class Persona():
    # Como la clase no tiene atributos, colocamos pass
    pass
    # Primer método, constructor __init__
    def __init__(self, nombre, año):
        # Atributos del método
        self.nombre = nombre
        self.año = año
    
    # Creacion de métodos
    def descripcion(self):
        # format, es usado para mostrar el contenido de los atributos, en el orden ue se ingresan en el parentesis
        return '{}, tiene {} años'.format(self.nombre, self.año)
    
    def comentario(self, frase):
        # Funciones para atributos
        return '{} dice: {}'.format(self.nombre, frase)

n = input('Ingrese su Nombre: ')
a = int(input('Ingrese su edad: '))

# Creacion del objeto
doctor = Persona(n,a)

print(doctor.descripcion())
print(doctor.comentario('Hola que tal!'))