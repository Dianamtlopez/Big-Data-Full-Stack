def nota_numerica(letra):
    letras = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'C+', 'C', 'F']
    notas = [4, 4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0]
    
    puntero = 0
    
    while letras[puntero] != letra:
        puntero += 1
    return notas[puntero]

num_notas = 0
sum_notas = 0

nota = input("Ingrese la nota de auerdo a la siguiente informacion:\n['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'C+', 'C', 'F'],\npara terminar pulse enter: \n")
nota = nota.upper()

while nota != "":
    try:
        valor_nota = nota_numerica(nota)
        num_notas += 1
        sum_notas += valor_nota
    except IndexError:
        #TODO: IMPRIMIR AVISO
        print("La nota",nota,"Es Incorrecta, vuelva a intentarlo...\n")
    
    nota = input("Ingrese la nota de auerdo a la siguiente informacion:\n['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'C+', 'C', 'F'],\npara terminar pulse enter: \n")
    nota = nota.upper()

if num_notas == 0:
    print("No se han introducido datos")
else:
    media = round(sum_notas / num_notas,2)
    print("\nLa nota final es:",media)