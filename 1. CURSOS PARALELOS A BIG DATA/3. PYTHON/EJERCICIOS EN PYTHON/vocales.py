#INTRODUCIR DATOS
nombre = input("Ingrese su nombre: ")

#FUNCION
def mayuscula(nombre):
    nombre = nombre.upper()
    return nombre

for caracter in mayuscula(nombre):
    print(caracter)
    
vocales = ''
for caracter in nombre:
    if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
        vocales += caracter
        vocales = vocales.upper()
    
print("\nEl nombre",mayuscula(nombre),"se compone de las siguientes vocales:",vocales)