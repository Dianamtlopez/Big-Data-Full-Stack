class Calculadora:
    #Creacion de métodos
    #self hace referencia a un determinado objeto
    # init significa inicializar
    def __init__(self, n1, n2):
        # Asignar atributos
        self.suma = (n1 + n2)
        self.resta = (n1 - n2)
        self.mult = (n1 * n2)
        self.div = (n1 / n2)

ope = int(input("INGRESE LA POPERACION DESEADA:\nPARA LA SUMA 1\nPARA LA RESTA 2\nPARA LA MULTIPLICACION 3\nPARA LA DIVISION 4\n"))

# Impresión del resultado
while ope > 0 and ope <= 4:
    num1 = float(input("Ingrese el primer valor: "))
    num2 = float(input("Ingrese el segundo valor: "))
    # Creacion del objeto para acceder al método
    operacion = Calculadora(num1, num2)
    if ope == 1:
        print("La Suma de",num1,"+",num2,"es:",operacion.suma,"\n")
    elif ope == 2:
        print("La Resta de",num1,"-",num2,"es:",operacion.resta,"\n")
    elif ope == 3:
        print("La Multiplicacion de",num1,"*",num2,"es:",operacion.mult,"\n")
    elif ope == 4:
        print("La División de",num1,"/",num2,"es:",operacion.div,"\n")
    
    opcion = input("Desea realizar otra operacion? S/N:")
    opcion = opcion.upper()
    if(opcion == 'S'):
        ope = int(input("INGRESE LA POPERACION DESEADA:\nPARA LA SUMA 1\nPARA LA RESTA 2\nPARA LA MULTIPLICACION 3\nPARA LA DIVISION 4\n"))
    else:
        ope = int(input("Para salir de la aplicación presione un numero diferente a las opciones de las operaciones:"))
print("Usted ha salido de la aplicación, adios...")
