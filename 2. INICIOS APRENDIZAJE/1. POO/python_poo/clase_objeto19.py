# Encapsulamiento, es la ocultacion de datos del estado interno, para proteger la integridad del objeto
# Se usa para proteger los valores de clases externas

class Cliente:
    def __init__(self):
        # Encapsular variables
        self.__codigo = 4321

    # Método encapsulado
    def __cuenta(self):
        print('Cuenta de Procesamiento...')
        
    def getcodigo(self):
        # Para desencapsular
        return self.__codigo
    
    
# Para que esta clase funcione, es necesario crear un objeto
# persona = Cliente()
# De esta forma no se puede acceder al valor cuando está encapsulado
# print(persona.__codigo)

# Acceder a variables y métodos encapsulados
persona = Cliente()
# Python, protege los atributos, cambiando el nombre internamente
# para poder hacer llamados se requiere de objeto._nombreclase__ombreatributo
print(persona._Cliente__codigo)
# llamado del método
persona._Cliente__cuenta()