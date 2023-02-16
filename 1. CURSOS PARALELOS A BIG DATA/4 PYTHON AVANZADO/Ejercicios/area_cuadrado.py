# Parámetros de Función

def calcular_area_cuadrado(lado):
    # Como parametros, esta función va a recibir el lado del cuadrado
    # Se define el docstring que es la documentación de la función
    """Calcular el área de un cuadrado"""
    area = lado * lado
    # Rernar el área calculada
    return area

# Captura de datos
l = int(input("Ingrese el valor del lado del cuadrado: "))
# l = Parámetro
# valor que el usuario ingresa = al argumento

# Invocamos la función
area_cuadrado = calcular_area_cuadrado(l)
# Visualizar datos
print(f'El área del cuadrado es: {area_cuadrado}')