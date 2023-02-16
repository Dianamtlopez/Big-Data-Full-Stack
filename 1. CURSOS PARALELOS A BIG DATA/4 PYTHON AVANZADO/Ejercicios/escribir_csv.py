# Archivos csv
import csv

# Vamos a almacenar datos de personas, su nombre, su apellido y su edad
# Creacion de columnas
columnas = ["nombre", "apellido", "edad"]
dato = ["paco", "Botero", 26]

datos_lista = [
    ["Paco", "Botero", 26],
    ["Javier", "Quiñonez", 24],
    ["Emilio", "Tafur", 25]
]

datos_dic = [
    {"nombre": "Paco", "apellido": "Botero", "edad": 26},
    {"nombre": "Javier", "apellido": "Quiñonez", "edad": 24},
    {"nombre": "Emilio", "apellido": "Tafur", "edad": 25}
]

'''
archivo = open("csv/datos.csv", "w")
writer = csv.writer(archivo, delimiter = ",")
archivo.close()
'''

# Otra forma con with, asignamos el alias al archivo y definimos el writer
# newline indica que no queremos una linea bacía cada vez que cambiemos de fila
with open("csv/datos.csv", "w", newline = "") as archivo:
    '''
    # Para escribir listas
    writer = csv.writer(archivo, delimiter = ",")
    # para escribir la primera fila escribimos que significa escribir una fila:
    writer.writerow(columnas)
    # Para escribir la primera fila de datos
    writer.writerow(dato)
    # Para escribir mas datos, enviamos una lista anidada
    writer.writerows(datos_lista)
    '''
    # para escribir diccionarios
    writer = csv.DictWriter(archivo, fieldnames = columnas)
    # Para que nos escriba la primera fila con los nombres de las columnas
    writer.writeheader()
    # Para escribir mas datos, enviamos una lista de diccionario anidada
    writer.writerows(datos_dic)
