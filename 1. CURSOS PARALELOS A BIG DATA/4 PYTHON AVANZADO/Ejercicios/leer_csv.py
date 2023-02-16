# Archivos csv
import csv
'''
# Para leer el archivo, despues de la r, encoding="UTF-8", en este caso no lo acepta
with open("csv/datos.csv", "r") as archivo:
    # Lector que permite pasar por las filas y extraer la informacion.
    reader = csv.reader(archivo)
    # Para evitar leer la primera fila del archivo csv, usamos la funcion next
    # Podemos almacenar las columnas a una variable para facilitar la lectura
    columnas = next(reader)
    print("Columnas",columnas)
    # Para extraer cada fila se itera sobre cada fila en el objeto reader creado
    for fila in reader:
        # print(fila[0], fila[1], fila[2])
        print(fila)
'''        
# Otra manera de leer archivos csv
with open("csv/datos.csv", "r") as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        # print(fila["nombre"], fila["apellido"], fila["edad"])
        print(fila)