# Método constructor

# Modificar un atributo

class Email:
    # Definir el constructor
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

# Creacion del Objeto
mi_correo = Email()

# Mostrar atributos del constructor
print(mi_correo.enviado)
# mostrar variable de un método cualquiera
mi_correo.enviar_correo()
print(mi_correo.enviado)