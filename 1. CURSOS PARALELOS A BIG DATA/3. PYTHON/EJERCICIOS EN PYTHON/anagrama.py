#TOMA DE DATOS
p1 = input("Ingrese la primera palabra: ")
p2 = input("Ingrese la segunda palabra: ")

#SE USA LISTA PORQUE IMPORTA ORDEN DE ELEMENTOS Y ADEMAS ES INMUTABLE
#FUNCION
def tacha(caracter, palabra):
    lpalabra = list(palabra)
    lpalabra.remove(caracter)
    return ''.join(lpalabra)
    
def es_anagrama(p1, p2):
    for letra in p1:
        if letra in p2:
            #SE ASIGNA A P2 LA NUEVA PALABRA PARA SER MODIFICADA
            p2 = tacha(letra, p2)
        else:
            return False
    #ESTO ES EQUIVALENTE
    if p2 == "":
        return True
    else:
        return False
    #A ESTO ES EQUIVALENTE
    #return p2 == ""

#IMPRIMIR RESULTADOS
if(es_anagrama(p1,p2) == True):
    print("La cadena Ingresada es un Anagrama!")
else:
    print("La cadena Ingresada no es un Anagrama!")