#TOMA DE DATOS
p1 = input("Ingrese la primera palabra: ")
p2 = input("Ingrese la segunda palabra: ")

#SE USA LISTA PORQUE IMPORTA ORDEN DE ELEMENTOS Y ADEMAS ES INMUTABLE
#FUNCION
def tacha(caracter, palabra):
    lpalabra = list(palabra)
    lpalabra.remove(caracter)
    return ''.join(lpalabra)

def frecuencias(palabra):
    resultado = {}
    for letra in palabra:
        if letra in resultado:
            resultado[letra] += 1
        else:
            resultado[letra] = 1
    return resultado

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
    
def es_anagrama_by_dic(p1, p2):
    fp1 = frecuencias(p1)
    fp2 = frecuencias(p2)
    return fp1 == fp2

#IMPRIMIR RESULTADOS
if(es_anagrama(p1,p2) == True):
    print("La cadena Ingresada es un Anagrama!")
else:
    print("La cadena Ingresada no es un Anagrama!")

if(es_anagrama_by_dic(p1,p2) == True):
    print("La cadena Ingresada es un Anagrama! comprobado por diccionario")
else:
    print("La cadena Ingresada no es un Anagrama! comprobado por diccionario")


print(frecuencias(p1))
print(frecuencias(p1))