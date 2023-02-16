def calcular_area_cuadrado(lado):
    # Como parametros, esta función va a recibir el lado del cuadrado
    # Se define el docstring que es la documentación de la función
    """Calcular el área de un cuadrado"""
    area = lado * lado
    # Rernar el área calculada
    return area

lado_cuadrados = [1, 3, 4]
area_cuadrado = []

for lado in lado_cuadrados:
    # Invocamos la función
    area = calcular_area_cuadrado(lado)
    area_cuadrado.append(area)
