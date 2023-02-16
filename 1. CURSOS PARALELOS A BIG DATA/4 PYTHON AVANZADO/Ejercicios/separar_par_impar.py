# Diferencia de lambda y función normal

def separar_par_impar(lista_numeros):
    pares = []
    impares = []
    for numero in lista_numeros:
        if numero %2 == 0:
            pares.append(numero)
        elif numero %2 != 0:
            impares.append(numero)
    return f'Lista de pares: {pares}\nLista de Impares: {impares}'

tamaño = int(input('Ingrese el tamaño de la lista a evaluar: '))

ln = []
i = 0
while i < tamaño:
    # Capturar datos
    ln.append(int(input('Ingrese el numero a evaluar: ')))
    i += 1

print(f'Lista Ingresada: {ln}')

# Invocar la funcion
evaluar_numero = separar_par_impar(ln)
print(evaluar_numero)
    
def calcular_are_cuadrado(lado):
    return lado ** 2
area = calcular_are_cuadrado(3)
print(area)

# Convertimos la funcion más fácil a lambda
lambda_area = lambda lado: lado ** 2
print(lambda_area(3))