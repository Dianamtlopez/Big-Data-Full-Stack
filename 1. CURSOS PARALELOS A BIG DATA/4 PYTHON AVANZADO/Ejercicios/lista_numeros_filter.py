# Funcion filter
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8]

# Funcion lambda que evalúa si un numero es divisible por 2, forma habitual
lista_pares = lambda numero: numero %2 == 0
#print(lista_pares(2))

# Pasamos toda la lista a traves de un filtro, el cual el filtro es la expresion
# lambda que nos permite evaluar si cada numero de la lista es o no un numero par
# y para ver el resultado del filter, lo debemos convertir a tipo lista usando la funcion list()
lista_pares = list(filter(lambda numero: numero %2 == 0, lista_numeros))
print(lista_pares)

lista_impares = list(filter(lambda numero: numero %2 != 0, lista_numeros))
print(lista_impares)

listas_pares = list(filter(lambda numero: numero %2 == 0, lista_numeros))
print(lista_pares)