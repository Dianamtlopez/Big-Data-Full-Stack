#import f_retenciones
#ES EQUIVALENTE A:
from f_retenciones import *

#OBTENER DATOS DE ENTRADA
sueldo = float(input("Sueldo: "))
situacion = input("Situacion (1/2/3): ")
num_hijos = int(input("Numero de hijos: "))

#OBTENER EXENCION
#exencion = f_retenciones.obtener_exencion(situacion, num_hijos)
#ES EQUIVALENTE A:
exencion = obtener_exencion(situacion, num_hijos)

sueldo_a_retener = sueldo - exencion

#OBTENER RETENCION
#porcentaje = f_retenciones.obtener_retencion(sueldo_a_retener)
#ES EQUIVALENTE A:
porcentaje = obtener_retencion(sueldo_a_retener)

monto_anual = sueldo_a_retener * porcentaje / 100
monto_mensual = monto_anual / 12

#MOSTRAR RESULTADOS
print("\nEl Sueldo es:\t\t\t",sueldo)
print("La Situacion es:\t\t",situacion)
print("La Base a Retener es:\t\t",sueldo_a_retener)
print("El porcentaje es:\t\t",porcentaje)
print("El Total Anual es:\t\t",monto_anual)
print("\nLa Retencion Mensual es:\t",monto_mensual)