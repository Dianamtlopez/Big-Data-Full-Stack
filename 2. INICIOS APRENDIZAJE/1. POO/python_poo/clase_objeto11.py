# HERENCIA MULTIPLE
# CONSISTE EN CREAR UNA CLASE A PARTIR DE MULTIPLES CLASES SUPERIORES
# HERENCIA MULTINIVEL
# CONSISTE EN QUE LA CLASE BASE Y LA DERIVADA, SE HEREDAN EN LA NUEVA DERIVADA

class Telefono:
    # Constructor de la clase Telefono
    def __init__(self):
        pass
    
    def llamar(self):
        print('Llamando...')
    def ocupado(self):
        print('Ocupado...')
    
class Camara:
    # Constructor de la clase Camara
    def __init__(self):
        pass
    
    def fotografia(self):
        print('Tomando fotos...')
    
class Reproduccion:
    # Constructor de la clase Reproduccion
    def __init__(self):
        pass
    
    def reproduccion_Musica(self):
        print('Reproduciendo música...')
    def reproducir_Video(self):
        print('Reproduciendo video...')
        
# Herencia ultiple: Consiste en tener una clase, la cual enlace, las clases superiores

class Smart_Phone(Telefono, Camara, Reproduccion):
    def __del__(self):
        print('Telefono apagado...')
        # Eliminar de memoria cuando no estan en uso (destructor)
        # Se usa como ahorro de memoria para optimizar ejercicios

# Se crea el objeto para hacer el llamado a las clases
# Se llama a la clase Smart Phone, porque en esta clase ya se encuentran las 3 clases
movil = Smart_Phone()
# Para saber qué métodos especiales, podemos utilizar o qué acciones puedo aplicarle al objeto
# print(dir(movil))
print(movil.llamar())
print(movil.ocupado())
print(movil.fotografia())
print(movil.reproduccion_Musica())
print(movil.reproducir_Video())
print(movil.__del__())