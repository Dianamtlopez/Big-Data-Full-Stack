nombre = input("Dame un nombre: ")

def extrae_vocales(name):
    vocales = ""
    for char in nombre:
        if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            vocales += char
    
    return vocales
        
print(extrae_vocales(nombre))