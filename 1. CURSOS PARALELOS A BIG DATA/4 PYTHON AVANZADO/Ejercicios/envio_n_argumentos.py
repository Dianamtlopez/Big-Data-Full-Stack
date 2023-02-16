# Parámetros *args

def calcular_perimetro(lista):
    # Hace referencia al parametro *args que va a recibir todos los datos a través de una tupla 
    # Parametros son los lados del cuadrilatero
    # docstring que es la documentación de la función
    """Calcular Perímetro de un cuadrilatero"""
    perimetro = 0
    # Iterar sobre cada uno de los valores del parámetro args
    for lado in lista:
        # Acumulamos el valor de cada lado dentro de perímetro
        perimetro += lado
    # Retornar el perímetro calculado
    return perimetro

# Seleccionar la figura deseada
figura = int(input('Ingrese la cantidad de lados de la figura: '))

lista = []
i = 0
# Captura de datos
while i < figura:
    lista.append(int(input('Ingrese el valor del lado: ')))
    i += 1

# Invocamos la función
valor_perimetro = calcular_perimetro(lista)
print(f'el valor del perímetro de la figura de {figura} lados es: {valor_perimetro}')