#INTRODUCIR DATOS
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))

#LISTA
meses_ano = [31,28,31,30,31,30,31,31,30,31,30,31]

#CONTAR LOS DÍAS
contador_dia = 0
contador_mes = 0

while(contador_mes < mes-1):
    contador_dia = (contador_dia + meses_ano[contador_mes])
    contador_mes = (contador_mes + 1)
    
contador_dia = contador_dia + dia 

#IMPRIMIR DATOS
print("a los",dia,"días, del mes",mes,"hay:",contador_dia,"días transcurridos")