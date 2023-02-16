# se utiliza en la herencia multiple, dando enfasis a la clase hija

class Mamifero:
    def __init__(self, nombre):
        print(f'{nombre}, Es un animal de sangre caliente.')

class Leon(Mamifero):
    def __init__(self):
        super().__init__('Simba')
        print('Es un mamífero y tiene cuatro patas.')
        
animal = Leon()