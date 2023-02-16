class Ropa:
    #Creacion de métodos
    #self hace referencia a un determinado objeto
    # init significa inicializar
    def __init__(self):
        # Asignar atributos
        self.marca = input("Ingrese la marca: ")
        self.talla = input("Ingrese la talla: ")
        self.color = input("Ingrese la el color: ")

# Creacion del objeto para acceder al método
camisa = Ropa()

# Impresión del resultado
print("\nHola, de la camisa, ha seleccionado: \nMarca:",camisa.marca,"\nTalla:",camisa.talla,"\nColor:",camisa.color)