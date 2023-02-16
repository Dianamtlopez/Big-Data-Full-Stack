def nota_numerica(letra):
    letras = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'C+', 'C', 'F']
    notas = [4, 4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0]
    
    puntero = 0
    
    while letras[puntero] != letra:
        puntero += 1
    return notas[puntero]

def pedir_nota_correcta():
    valor_nota=""
    while valor_nota == "":
        #EQUIVALE A:
        #nota = input("Nota: ").upper()
        nota = input("Ingrese la nota de auerdo a la siguiente informacion:\n['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'C+', 'C', 'F'],\npara terminar pulse enter: \n")
        nota = nota.upper()
        try:
            valor_nota = nota_numerica(nota)
        except IndexError:
            valor_nota = ""
            print("Nota incorrecta",nota,"debe ingresarla de Nuevo")
    
    return valor_nota

def pedir_numero():
    
    valor = ""
    while valor == "":
        try:
            valor = int(input("Ingrese la cantidad de asignaturas: "))
        except ValueError:
            valor = ""
            print("Error, debe ser un numero entero, vuelva a introducirlo")    
        while valor <= 0:
            print("Error, debe ingresar numeros mayores que cero!")
            valor = int(input("Ingrese la cantidad de asignaturas: "))
    return valor

num_nota = pedir_numero()
sum_nota = 0

for i in range(num_nota):
    print("Nota",i+1)
    valor_nota = pedir_nota_correcta()
    
    sum_nota += valor_nota

if num_nota == 0:
    print("No se ha introducido datos!")
else:
    media = round(sum_nota / num_nota,2)
    print("\nLa nota final es:",media)