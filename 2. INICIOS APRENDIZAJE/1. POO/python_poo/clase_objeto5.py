# Funciones para atributos
class Persona():
    edad = int(input("Ingrese la edad: "))
    nombre = input("Ingrese el nombre: ")
    pais = input("Ingrese el pais: ")

# Crear un objeto
doctor = Persona()

# Llamar a los atributos mediante el objeto creado
print("\nHola",doctor.nombre,"Tienes",doctor.edad,"años, de nacionalidad",doctor.pais)
# Uuso de funciones
print("\nHola",getattr(doctor, 'nombre'),"Tienes",getattr(doctor, 'edad'),"años.","de nacionalidad",getattr(doctor, 'pais'))

# funcion que devuelve si existe o no algún atributo
print("La variable edad existe?", hasattr(doctor, 'edad'))
print("La variable nombre existe?", hasattr(doctor, 'nombre'))
print("La variable pais existe?", hasattr(doctor, 'pais'))

#Funcion que cambia informacion de los atributos
setattr(doctor, 'nombre', 'Andrea')
print("El nuevo nombre es:",doctor.nombre)

# Para eliminar un atributo dentro de una clase
delattr(Persona, 'pais')
print("La variable pais existe?", hasattr(doctor, 'pais'))