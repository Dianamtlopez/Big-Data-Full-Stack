class Cancion:
    # Lista de palabras a evaluar
    cancion = ['Los aviones', 'viajar', 'la mañana', 'el viento', 'soñar', 'la mar']
    # para la palabra que contiene los, agrega un  texto y para el resto de palabras, otro texto
    for texto in cancion:
        if 'Los' in texto:
            print(f'Me gustan {texto}, me gustas tú')
        else:
            print(f'Me gusta {texto}, me gustas tú')
