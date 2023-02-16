# Funcion map()

def calcular_cuadrado(numero):
    return numero ** 2

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""lista_cuadrados = []

for numero in lista_numeros:
    cuadrado = calcular_cuadrado(numero)
    lista_cuadrados.append(cuadrado)
    
print(lista_cuadrados)"""
# Las siguientes dos lineas, hacen lo mismo que el código anterior
map_cuadrados = list(map(calcular_cuadrado, lista_numeros))
print(map_cuadrados)
