#LIBRERIA
import string

#INGRESO DE DATOS
cadena = input("Digite la cadena: ")

#FUNCION PALINDROMO
def es_palindromo(cadena):
    cadena = cadena.replace(" ","")
    cadena = cadena.lower()
    cadena = cadena.replace("á","a")
    cadena = cadena.replace("ä","a")
    cadena = cadena.replace("é","e")
    cadena = cadena.replace("ë","e")
    cadena = cadena.replace("í","i")
    cadena = cadena.replace("ï","i")
    cadena = cadena.replace("ó","o")
    cadena = cadena.replace("ö","o")
    cadena = cadena.replace("ú","u")
    cadena = cadena.replace("ü","u")
    #REEMPLAZAR SIGNOS DE PUNTUACION POR NADA
    cadena = cadena.translate(str.maketrans('', '', string.punctuation))
       
    '''Es equivalente a
    if cadena == cadena[::-1]
        return True
    else:
        resturn False'''
    
    return cadena == cadena[::-1]

#IMPRIMIR INFORMACION
if(es_palindromo(cadena)==True):
    print("La cadena Ingresada es Palindromo!")
else:
    print("La cadena Ingresada no es Palindromo!")