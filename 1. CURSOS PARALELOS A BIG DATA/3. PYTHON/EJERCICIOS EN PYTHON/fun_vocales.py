#INTRODUCIR DATOS
nombre = input("Ingrese su nombre: ")

#FUNCIONES
def mayuscula(nombre):
    nombre = nombre.upper()
    return nombre

for caracter in mayuscula(nombre):
    print(caracter)
    
vocales = ''
def extraer_vocales(vocales):
    for caracter in nombre:
        if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u' or caracter == 'A' or caracter == 'E' or caracter == 'I' or caracter == 'O' or caracter == 'U':
            vocales += caracter
            vocales = vocales.upper()
    return vocales

#MOSTRAR RESULTADOS
print("\nEl nombre",mayuscula(nombre),"se compone de las siguientes vocales:",extraer_vocales(vocales))