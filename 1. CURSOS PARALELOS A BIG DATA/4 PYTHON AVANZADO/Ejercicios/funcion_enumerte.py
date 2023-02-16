# Función enumerate
"""enumerate(iterale, start=0)"""

nombres = ["Paco", "Emilio", "Javier", "Ana"]
# Siempre tener presente que se nos visualiza es el objeto, por tanto
# tenemos que convertir a lista, para visualizar el objeto
nombres_enumerados = list(enumerate(nombres))
print(nombres_enumerados)

# Para iniciar la cuenta en otro valor, se hace de la siguiente manera:
nombres_enumerados = list(enumerate(nombres, start = 5))
print(nombres_enumerados)

for indice, elemento in enumerate(nombres):
    print(indice, elemento)
