# Funcion list_comprehension

"""lista = [expresión(elemento) for elemento in objeto_iterable]"""

def calcular_cuadrado(numero):
    return numero ** 2

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_cuadrados = []

for numero in lista_numeros:
    cuadrado = calcular_cuadrado(numero)
    lista_cuadrados.append(cuadrado)
    
print("Ciclo for: ", lista_cuadrados)

lista_comprehension = [calcular_cuadrado(num) for num in lista_numeros]
print("Lista comprehension",lista_comprehension)
