#SUELDOS
sueldos = (12450, 20200, 35200, 60000, 70000, 100000, 10000000)
retenciones = (1.55, 13.32, 20.08, 26.84, 29.91, 33.94, 44.88)

def buscaRetencion(s):
    ix = 0
    # PARA COMPROBAR EL AND, AMBAS PREMISAS DEBEN SER VERDADERAS,
    # CUANDO UNA ES FALSA, SE SALE Y NO EVALUA LA SIGUIENTE, POR LO TANTO,
    # HAY QUE COLOCAR LA QUE SIEMPRE ES VERDADERA DE PRIMERA Y AL FINAL LA QUE PRIMERO VA A FALLAR
    while ix < 7 and s >= sueldos[ix]:
        ix += 1

    if ix == 0:
        retencion = 0
    elif ix > 6:
        retencion = 45
    else: 
        retencion = retenciones[ix-1] + (((s - sueldos[ix-1]) * (retenciones[ix] - retenciones[ix-1]))/(sueldos[ix] - sueldos[ix-1]))

    return retencion

def netoAnual(s, r):
    retencionTotal = r + 6.35
    miSueldoNeto = s * (100 - retencionTotal)/100
    return miSueldoNeto

strMiSueldo = (float(input("Introduce Sueldo: ")))

#BUSQUEDA DE LIMITES
retencion = buscaRetencion(strMiSueldo)

#CALCULO DE PAGAS
miSueldoNeto = netoAnual(strMiSueldo, retencion)

mensual12 = miSueldoNeto / 12
mensual14 = miSueldoNeto / 14

print("12 pagas de:", round(mensual12,2))
print("14 pagas de:", round(mensual14,2))