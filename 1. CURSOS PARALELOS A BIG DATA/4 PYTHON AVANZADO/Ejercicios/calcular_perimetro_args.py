# Parámetros *args
# Con esta función, a la hora de enviar los argumentos, debemos hacerlo con un numero determinado de valores

def calcular_perimetro(*args):
    # Hace referencia al parametro *args que va a recibir todos los datos a través de una tupla 
    # Parametros son los lados del cuadrilatero
    # docstring que es la documentación de la función
    """Calcular Perímetro de un cuadrilatero"""
    perimetro = 0
    # Iterar sobre cada uno de los valores del parámetro args
    for lado in args:
        # Acumulamos el valor de cada lado dentro de perímetro
        perimetro += lado
    # Retornar el perímetro calculado
    return perimetro

# Seleccionar la figura deseada
figura = int(input('Ingrese la figura deseada:\n1 Triangulo:\n2 Cuadrilatero:\n3 Pentagono:\n'))

if figura == 1:
    l1 = int(input("Ingrese Lado 1 del triangulo: "))
    l2 = int(input("Ingrese Lado 2 del triangulo: "))
    l3 = int(input("Ingrese lado 3 del triangulo: "))
    # Invocamos la función
    valor_perimetro = calcular_perimetro(l1, l2, l3)
    # Visualizacion de la figura
    print(f'el valor del perímetro del triangulo es: {valor_perimetro}')
elif figura == 2:
    l1 = int(input("Ingrese Lado 1 del cuadrilatero: "))
    l2 = int(input("Ingrese Lado 2 del cuadrilatero: "))
    l3 = int(input("Ingrese lado 3 del cuadrilatero: "))
    l4 = int(input("Ingrese lado 4 del cuadrilatero: "))
    # Invocamos la función
    valor_perimetro = calcular_perimetro(l1, l2, l3, l4)
    # Visualizacion de la figura
    print(f'el valor del perímetro del cuadrilatero es: {valor_perimetro}')
elif figura == 3:
    l1 = int(input("Ingrese Lado 1 del pentagono: "))
    l2 = int(input("Ingrese Lado 2 del pentagono: "))
    l3 = int(input("Ingrese lado 3 del pentagono: "))
    l4 = int(input("Ingrese lado 4 del pentagono: "))
    l5 = int(input("Ingrese lado 5 del pentagono: "))
    # Invocamos la función
    valor_perimetro = calcular_perimetro(l1, l2, l3, l4, l5)
    # Visualizacion de la figura
    print(f'el valor del perímetro del pentagrama es: {valor_perimetro}')
else:
    print("Figura no catalogada...")