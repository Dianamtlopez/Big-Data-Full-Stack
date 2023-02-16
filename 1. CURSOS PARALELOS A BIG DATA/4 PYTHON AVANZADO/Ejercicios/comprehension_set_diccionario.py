# Funcion comprehension para set y diccionarios, la unica diferencia es que se escribe es dentro de {}

lista_numeros = [1, 2, 3, 4, 1, 2, 5, 6, 7, 8, 9, 10]

# Recordad que los set no contienen elementos repetidos
set_pares = {num for num in lista_numeros if num % 2 == 0}
print(set_pares)

vocales = "aeiou"
diccionario = {vocal.upper(): vocal.lower() for vocal in vocales}
print(diccionario)

