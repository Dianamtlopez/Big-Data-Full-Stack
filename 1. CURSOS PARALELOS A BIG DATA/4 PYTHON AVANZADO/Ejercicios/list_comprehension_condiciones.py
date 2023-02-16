# Funcion list_comprehension
"""
    lista = [expresión(elemento) for elemento in objeto_iterable if condición]
    lista = [expresión(condición) for elemento in objeto_iterable]
"""

def calcular_cuadrado(numero):
    return numero ** 2

def es_par(numero):
    return numero % 2 == 0

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_cuadrados = [calcular_cuadrado(num) for num in lista_numeros]
print("Lista comprehension",lista_cuadrados)

# Primera forma
lista_cuadrados_pares = [calcular_cuadrado(num) for num in lista_numeros if es_par(num)]
print(lista_cuadrados_pares)

# segunda forma
lista_resultados = [calcular_cuadrado(num) if es_par(num) else 0 for num in lista_numeros]
print(lista_resultados)
