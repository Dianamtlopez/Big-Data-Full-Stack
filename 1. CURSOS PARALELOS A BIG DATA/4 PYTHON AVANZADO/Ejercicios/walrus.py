# Walrus

def calcular_cuadrado(numero):
    return numero ** 2

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []
impares = []
'''
for num in lista_numeros:
    cuadrado = calcular_cuadrado(num) 
    if cuadrado %2 == 0:
        pares.append(cuadrado)
        print(f'el cuadrado de {num} es {cuadrado} y es número par.')
    elif cuadrado %2 != 0:
        impares.append(cuadrado)
        print(f'el cuadrado de {num} es {cuadrado} y es número impar.')

print(pares)
print(impares)

for num in lista_numeros: 
    if(cuadrado := calcular_cuadrado(num)) %2 == 0:
        pares.append(cuadrado)
        print(f'el cuadrado de {num} es {cuadrado} y es número par.')
    elif(cuadrado := calcular_cuadrado(num)) %2 != 0:
        impares.append(cuadrado)
        print(f'el cuadrado de {num} es {cuadrado} y es número impar.')

print(pares)
print(impares)
'''
pares_comprehension = [cuadrado for num in lista_numeros if(cuadrado := calcular_cuadrado(num)) num % 2 == 0]
print(pares_comprehension)
