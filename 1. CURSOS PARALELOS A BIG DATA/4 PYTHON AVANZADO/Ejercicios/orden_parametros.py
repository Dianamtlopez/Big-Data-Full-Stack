# Orden de parámetros

def parametros_ordenados(nombre, apellido, *argas, **kwargs):
    print(nombre, apellido, argas, kwargs)

n = input('Ingrese su nombre: ')
a = input('Ingrese su apellido: ')
e = input('ingrese su edad: ')
d = input('Ingrese su documento: ')

# Invocación de la funcion, se hace envio en orden de parámetro y kwargs
# debe enviarse en forma de Diccionario
parametros_ordenados(n, a, e, documento = d)