#CREACION DE LAS LISTAS

RANGOS = [0, 12450, 20200, 35200, 60000, 300000]
PORCENTAJES = [0, 19, 24, 30, 37, 45, 47]

#TABLA BIDIMENSIONAL - TABLA DE TABLAS
RETENCIONES = [[0, 0], [12450, 19], [20200, 24], [35200, 30], [60000, 37], [300000, 45], [float("inf"), 47]]

SIT1 = [0, 15947, 17100]
SIT2 = [15546, 16481, 17634]
SIT3 = [14000, 14516, 15063]

#TRANSFORMARLO EN DICCIONARIO
SITUACIONES = {
                '1': [0, 15947, 17100],
                '2': [15546, 16481, 17634],
                '3': [14000, 14516, 15063]
              }

#SE TRANSFORMA PORQUE ESTA ESTRUCTURA POR MEDIO DE IF ES MUY REPETITIVA
def obtener_exencion(sit, nhijos):
    if nhijos > 2:
        nhijos = 2
    elif nhijos < 0:
        nhijos = 0
        
    if sit == '1':
        return SIT1[nhijos]
    if sit == '2':
        return SIT2[nhijos]
    if sit == '3':
        return SIT3[nhijos]
    return 0

def obtener_exencion_DICCIONARIO(sit, nhijos):
    if nhijos > 2:
        nhijos = 2
    elif nhijos < 0:
        nhijos = 0
    
    return SITUACIONES[sit][nhijos]
    
def obtener_retencion(base):
    i = 0
    while i < len(RANGOS):
        if base <= RANGOS[i]:
            break
        i += 1
    return PORCENTAJES[i]

def obtener_retencion_for(base):
    i = 0
    for rango in RANGOS:
        if base <= rango:
            break
        i += 1
    return PORCENTAJES[i]

def obtener_retencion_for_RETENCIONES(base):
    i = 0
    for retencion in RETENCIONES:
        if base <= retencion[0]:
            return retencion[1]