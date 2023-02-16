#OBTENER DATOS DE ENTRADA
sueldo = float(input("Sueldo: "))
situacion = input("Situacion (1/2/3): ")
num_hijos = int(input("Numero de hijos: "))

#OBTENER EXENCION
exencion = 0
if situacion == '1':
    if num_hijos <= 0:
        exencion = 0
    elif num_hijos == 1:
        exencion = 15947
    else:
        exencion = 17100
    
if situacion == '2':
    if num_hijos <= 0:
        exencion = 15546
    elif num_hijos == 1:
        exencion = 16481
    else:
        exencion = 17634

if situacion == '3':
    if num_hijos <= 0:
        exencion = 14000
    elif num_hijos == 1:
        exencion = 14516
    else:
        exencion = 15063

sueldo_a_retener = sueldo - exencion

#OBTENER RETENCION
if sueldo_a_retener <= 12750:
    porcentaje = 19
elif sueldo_a_retener <= 20200:
    porcentaje = 24
elif sueldo_a_retener <= 35200:
    porcentaje = 30
elif sueldo_a_retener <= 60000:
    porcentaje = 37
elif sueldo_a_retener <= 300000:
    porcentaje = 45
else:
    porcentaje = 47



monto_anual = sueldo_a_retener*porcentaje/100
monto_mensual = monto_anual/12

#MOSTRAR RESULTADOS
print("\nEl Sueldo es:\t\t\t",sueldo)
print("La Situacion es:\t\t",situacion)
print("La Base a Retener es:\t\t",sueldo_a_retener)
print("El porcentaje es:\t\t",porcentaje)
print("El Total Anual es:\t\t",monto_anual)
print("\nLa Retencion Mensual es:\t",monto_mensual)