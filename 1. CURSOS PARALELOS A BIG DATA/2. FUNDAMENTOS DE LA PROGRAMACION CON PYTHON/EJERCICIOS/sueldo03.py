import lib_IRPF2018

strMiSueldo = (float(input("Introduce Sueldo: ")))

#BUSQUEDA DE LIMITES
retencion = lib_IRPF2018.buscaRetencion(strMiSueldo)

#CALCULO DE PAGAS
miSueldoNeto = lib_IRPF2018.netoAnual(strMiSueldo, retencion)

mensual12 = miSueldoNeto / 12
mensual14 = miSueldoNeto / 14

print("12 pagas de:", round(mensual12,2))
print("14 pagas de:", round(mensual14,2))