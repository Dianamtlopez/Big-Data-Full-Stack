def sumar(numero):
    new_sumar = []
    cont = 0
    while cont < len(numero):
        new_sumar.append(cont + numero[cont])
        cont += 1
    return new_sumar

seq = [2,2,3]
result = sumar(seq)
print(result)    