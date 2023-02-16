# Polimorfismo: mismo objeto con diferentes valores, el mismo nombre de sus atributos y métodos
# Pueden ser identicos pero sus acciones y funciones son diferentes

class Auto:
    # Objeto
    rueda = 4
    # Accion
    def desplazamiento(self):
        print('El auto se está desplazando sobre 4 ruedas')
        
class Moto:
        # Objeto
    rueda = 2
    # Accion
    def desplazamiento(self):
        print('La moto se está desplazando sobre 2 ruedas')