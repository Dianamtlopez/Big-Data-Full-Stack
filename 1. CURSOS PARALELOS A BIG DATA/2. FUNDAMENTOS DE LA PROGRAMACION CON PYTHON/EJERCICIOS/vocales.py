# defino funcion 
def extrae_vocales(cadena): 
    vocales='' 
    for caracter in cadena: 
        if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u': 
            vocales += caracter
    return vocales 

# datos 
palabra = input("Dime una palabra: ")
# funciona pra evaluar el uso de mayusculas y minusculas
palabra = palabra.lower()

# se crea el objeto para hacer el llamado
resultado = extrae_vocales(palabra)

# resultado: 
print(f"Las volcales de tu palabra son: {resultado}") 

