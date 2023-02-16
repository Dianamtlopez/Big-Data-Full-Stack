class Generacion:
    # Constructor de la clase Generacion
    def __init__(self, nacimiento):
        self.nacimiento = nacimiento

    # Método para verificar la generacion segun el año ingresado
    def verificar(self):
        if self.nacimiento >= 1919 and self.nacimiento <= 1944:
            print('Perteneces a la Generacion silenciosa1')
        elif self.nacimiento >= 1945 and self.nacimiento <= 1964:
            print('Perteneces a la Baby Boomer')
        elif self.nacimiento >= 1965 and self.nacimiento <= 1979:
            print('Perteneces a la Generacion X')
        elif self.nacimiento >= 1980 and self.nacimiento <= 2000:
            print('Perteneces a la Generacion Y')
        elif self.nacimiento >= 2001 and self.nacimiento <= 2010:
            print('Perteneces a la Generacion Z')
        else:
            print('No existe Generación para el año indicado')

an = int(input('Ingrese el año de nacimiento: '))        

# Creacion del Objeto
verif_gen = Generacion(an)

# Mostrar el resultado de la verificacion
verif_gen.verificar()