# Parámetros *args

def calcular_perimetro(lado1, lado2, lado3, lado4):
    # Parametros son los lados del cuadrilatero
    # docstring que es la documentación de la función
    """Calcular Perímetro de un cuadrilatero"""
    perimetro = lado1 + lado2 + lado3 + lado4
    # Retornar el perímetro calculado
    return perimetro

# Captura de datos
l1 = int(input('Ingrese el valor del lado 1: '))
l2 = int(input('Ingrese el valor del lado 2: '))
l3 = int(input('Ingrese el valor del lado 3: '))
l4 = int(input('Ingrese el valor del lado 4: '))

# Invocamos la función
valor_perimetro = calcular_perimetro(l1, l2, l3, l4)
print(f'el valor del perímetro del cuadrilatero es: {valor_perimetro}')