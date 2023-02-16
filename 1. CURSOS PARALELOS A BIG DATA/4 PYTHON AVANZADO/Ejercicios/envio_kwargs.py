# Parametro **kwargs

def funcion_kwargs(**kwargs):
    print(kwargs)
    # Podemos iterar a través de un ciclo for
    for llave, valor in kwargs.items():
        print(f'Llave: {llave}, Valor: {valor}')
    # Visulizar valores ingresados
    print(kwargs['nombre'], kwargs['apellido'], kwargs['documento'])

# Ingreso de datos
n = input('Ingrese su nombre: ')
a = input('Ingrese su apellido: ')
d = input('Ingrese su documento: ')
# Invocación de la funcion y el parámetro debe enviarse en forma de Diccionario
funcion_kwargs(nombre = n, apellido = a, documento = d)