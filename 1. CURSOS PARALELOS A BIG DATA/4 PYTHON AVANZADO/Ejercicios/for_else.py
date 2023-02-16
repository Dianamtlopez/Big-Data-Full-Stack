# Sentencia else en for

nombres = ["Paco", "Emilio", "Javier", "Ana"]

for nombre in nombres:
    print(nombre)
else:
    # se ejecuta unicamente cuando se itera sobre todos y cada uno de los elementos
    # del objeto iterable y el ciclo no se rompe
    print("Ciclo terminado")

for nombre in nombres:
    print(nombre)
    if nombre == "Javier":
        break
else:
    # se ejecuta unicamente cuando se itera sobre todos y cada uno de los elementos
    # del objeto iterable y el ciclo no se rompe, si se usa break, else no se ejecuta
    print("Ciclo terminado")
