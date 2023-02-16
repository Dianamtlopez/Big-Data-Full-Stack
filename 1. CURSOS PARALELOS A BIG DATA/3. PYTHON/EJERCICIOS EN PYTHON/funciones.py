def nota_numerica(letra):
    '''
        PIDE UNA NOTA EN FORMA DE LETRA Y DEVULEVE SU VALOR EN NUMERO DECIMAL.
        DA ERROR SI LA NOTA NO ESTA CORRECTA
    '''
    letras = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'C+', 'C', 'F']
    notas = [4, 4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0]
    
    puntero = 0
    letra = letra.upper()
    
    while letras[puntero] != letra:
        puntero += 1
        
    return notas[puntero]

def pedir_nota_correcta():
    '''
        PIDE UNA NOTA EN FORMA DE LETRA Y SI ES INCORRECTA VUELVE A PEDIRLA
        DEVULEVE SU VALOR EN NUMERO DECIMAL.
    '''
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
    '''
        PIDE UN VALOR POR PANTALLA. SI NO ES UN NUMERO, VUELVE A PEDIRLO.
        DEVULEVE EL NUMERO ENTERO INTRODUCIDO.
    '''
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