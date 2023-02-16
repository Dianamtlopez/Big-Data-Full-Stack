import funciones

num_nota = funciones.pedir_numero()
sum_nota = 0

for i in range(num_nota):
    print("Nota",i+1)
    valor_nota = funciones.pedir_nota_correcta()
    
    sum_nota += valor_nota

if num_nota == 0:
    print("No se ha introducido datos!")
else:
    media = round(sum_nota / num_nota,2)
    print("\nLa nota final es:",media)