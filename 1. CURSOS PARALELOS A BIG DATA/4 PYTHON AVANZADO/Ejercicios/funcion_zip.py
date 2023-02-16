# Función zip

nombres = ["Paco", "Emilio", "Javier"]
apellidos = ["Botero", "Tafur", "Quiñonez"]

# Con la función zip, unimos en tuplas cada nombre con su respectivo apellido
# zip(como argumentos enviamos los objetos iterables que queremos unir)
nombre_completo = list(zip(nombres, apellidos))
print(nombre_completo)

# el asterisco * permite desempaquetar en las dos variables seguido por la lista de tuplas
nombres_unzip, apellidos_unzip = zip(*nombre_completo)
print(nombres_unzip)
print(apellidos_unzip)

for nombre, apellido in zip(nombres, apellidos):
    # En cada iteracion, se imprime tanto el nombre como el apellido de las listas
    # ideal para procesos en los que debamos manejar multiples iterables al tiempo
    print(nombre, apellido)
    
    