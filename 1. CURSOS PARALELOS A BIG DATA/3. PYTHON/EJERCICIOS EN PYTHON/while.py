def nota_numerica(letra):
    letras = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'C+', 'C', 'F']
    notas = [4, 4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0]
    
    puntero = 0
    
    while letras[puntero] != letra:
        puntero += 1
    return notas[puntero]

consulta = input("Ingrese la letra deseada de auerdo a la siguiente informacion:\n['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'C+', 'C', 'F']: \n")
consulta = consulta.upper()
print("\nEl Valor que pertenece a la nota",consulta,"es:",nota_numerica(consulta))