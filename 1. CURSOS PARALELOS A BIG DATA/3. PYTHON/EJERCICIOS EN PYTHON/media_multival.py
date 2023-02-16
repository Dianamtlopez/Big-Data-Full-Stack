from funciones import nota_numerica

def media(*notas):
    suma_notas = 0
    for nota in notas:
        valor_nota = nota_numerica(nota)
        suma_notas += valor_nota
    
    if len(notas) > 0:
        return suma_notas / len(notas)

def multientrada(*valores):
    for valor in valores:
        print(valor * 2)
    
def boletin(**asignaturas):
    #notas = []
    for asignatura, nota in asignaturas.items():
        print(asignatura, "-", nota)
        #notas.append(nota)
    #ES EQUIVALENTE A notas= [] Y notas.append(nota)
    #CON ESTO SE CONVIERTE EL DICCIONARIO EN LISTA
    notas = list(asignaturas.values())
    nota_media = media(*notas)
    print("Media:", nota_media)

def multientrada_1(**pares_clave_valor):
    #print(pares_clave_valor)
    #FUNCION QUE TRABAJA CON UN DICCIONARIO
    for clave, valor in pares_clave_valor.items():
        print(clave, "-", valor)