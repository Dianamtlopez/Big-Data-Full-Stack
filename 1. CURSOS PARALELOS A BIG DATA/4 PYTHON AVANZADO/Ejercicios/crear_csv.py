# Archivos csv
import csv
# âra definir las rutas y que sean compatibles en todo sistema operativo
import os

# Rutas relativas: csv_vacio.csv, la cual está al mismo nivel del archivo python
# Rutas absolutas: D:/Users/User/Downloads/GLOVO/PYTHON AVANZADO/Ejercicios/csv/csv_vacio.csv
ruta = "csv/csv_vacio.csv"

ruta_absoluta = "D:/Users/User/Downloads/GLOVO/PYTHON AVANZADO/Ejercicios/csv/csv_vacio.csv"
# Siempre es recomendable usar la segunda ruta con la libreria os, ya qye esta nos garantiza
# la compatibilidad entre diferentes sistemas operativos

ruta_absoluta_os = os.path.join(os.getcwd(),"csv/csv_vacio.csv",)

# Vemos que ambas rutas son iguales, pues las dos apuntan a la misma direccion
print(ruta_absoluta)
print(ruta_absoluta_os)

# Abrir el archivo
# archivo_abierto = open(ruta, 'w')
# escribir en el archivo nombrada por convensió
# writer = csv.writer(archivo_abierto, delimiter=",")
# archivo_abierto.close()
