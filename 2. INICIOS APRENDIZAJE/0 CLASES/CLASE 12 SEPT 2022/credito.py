class Credito:
    # Constructor de la clase Generacion
    def __init__(self, edad, antiguedad, salario):
        self.edad = edad
        self.antiguedad = antiguedad
        self.salario = salario

    # Método para verificar las condiciones
    def verificar(self):
        if self.edad <= 18:
            if self.antiguedad >= 3 and self.salario > 2500:
                print('Reunes todos los requisitos para adquirir el crédito')
            else:
                if self.salario >= 4000:
                    print('No cuentas con la antiguedad necesaria pero tu salario\nes mayor o igual a 4.000 soles, por lo tanto,\nReunes todos los requisitos para adquirir el crédito')
                else:
                    print('No reunes los requisitos para adquirir el crédito')
        else:
            print('No Cuentas con la edad requerida para adquirir créditos')

# Captura de datos
e = int(input('Ingrese su edad: '))        
a = int(input('Ingrese la antiguedad en el banco expresada en años: '))
s = int(input('Ingrese su salario: '))

# Creacion del Objeto
verif_cred = Credito(e, a, s)

# Mostrar el resultado de la verificacion
verif_cred.verificar()