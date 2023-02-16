#INTRODUCIR DATOS
n = int(input("Ingrese la tabla deseada: "))
#FUNCIONES
tabla = ''
def generar_tabla(tabla):
    for m in range(1, 11):
        tabla += ("{:>2} x {} = {:>2}\n".format(m, n, m*n))    
    return tabla

#MOSTRAR RESULTADOS
print("la tabla de",n,"es:\n")
print(generar_tabla(tabla))