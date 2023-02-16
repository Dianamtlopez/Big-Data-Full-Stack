# Funcion filter
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8]

# Para aplicar la expresion lambda a cada elemento que pertenece a la lista, el primer argumento
# de la funcion es map, como segundo parametro, enviamos lista_numeros, para visualizarlo por
# medio del print, debemos convertirlo a una lista, de lo contrario se visualiza es el objeto creado
nueva_lista = list(map(lambda numero: numero * 10, lista_numeros))
print(nueva_lista)