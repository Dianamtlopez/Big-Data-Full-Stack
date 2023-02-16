#LISTA
meses_ano = [31,28,31,30,31,30,31,31,30,31,30,31]

#FUNCION
def es_bisiesto(year):
    if year % 4 != 0:
   #if not year % 4 == 0:
        return False
    
    if year % 100 == 0 and year % 400 != 0:
        return False
    
    return True

#INTRODUCIR DATOS
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

#COMPROBAR BISIESTO
#if es_bisiesto(anio) == True:
if es_bisiesto(anio): 
    meses_ano[1] = 29

#CONTAR LOS DÍAS
contador_dia = 0
contador_mes = 0

while(contador_mes < mes-1):
    contador_dia = (contador_dia + meses_ano[contador_mes])
    contador_mes = (contador_mes + 1)
    
contador_dia = contador_dia + dia 

#IMPRIMIR DATOS
print("a los",dia,"días, del mes",mes,"hay:",contador_dia,"días transcurridos6")