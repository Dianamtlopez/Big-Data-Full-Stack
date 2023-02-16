def obtener_exencion(sit, nhijos):
    exencion = 0
    if sit == '1':
        if nhijos <= 0:
            exencion = 0
        elif nhijos == 1:
            exencion = 15947
        else:
            exencion = 17100
        
    if sit == '2':
        if nhijos <= 0:
            exencion = 15546
        elif nhijos == 1:
            exencion = 16481
        else:
            exencion = 17634

    if sit == '3':
        if nhijos <= 0:
            exencion = 14000
        elif nhijos == 1:
            exencion = 14516
        else:
            exencion = 15063
    
    return exencion

def obtener_retencion(base):
    if base <= 0:
        porcentaje = 0
    elif base <= 12750:
        porcentaje = 19
    elif base <= 20200:
        porcentaje = 24
    elif base <= 35200:
        porcentaje = 30
    elif base <= 60000:
        porcentaje = 37
    elif base <= 300000:
        porcentaje = 45
    else:
        porcentaje = 47
    
    return porcentaje