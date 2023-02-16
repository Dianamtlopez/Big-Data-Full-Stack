# Funcion Range
"""range(inicio, fin, paso)"""

# enviamos un solo elemento y por defecto este elemento es el fin
# el inicio es cero y el paso 1
serie_1 = range(5)
# Nos muestra un objeto de tipo rango que nos dice en que numero inicia y en que numero finaliza
print(serie_1)
# Para poder ver la lista que compone la serie, debemos convertir la funcion a una lista
print(list(serie_1))

# Serie con inicio y con fin
serie_2 = range(5,10)
print(list(serie_2))

serie_3 = range(3, 10, 2)
print(list(serie_3))

for elemento in serie_3:
    print(elemento)
    
    