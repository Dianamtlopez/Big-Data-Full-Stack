# EJEMPLO PRACTICO DE HERENCIA
# Clase Padre
class Calculadora:
    # Introducimos el constructor
    def __init__(self, numero):
        # Caracteristicas o atributos de la calculadora
        self.n = numero
        # se crea un bucle para iterar desde cero hasta el numero que hayamos escogido, como cantidad de operandos
        self.datos = [0 for i in range(numero)] 
    # Método para llamar los datos
    def ingresardato(self):
        # ingresar los valores a operar
        self.datos = [int(input('Ingrese dato '+ str(i+1)+ ' = ')) for i in range(self.n)]
#Clase Hija        
class Ope_Basicas(Calculadora):
    def __init__(self):
        # Se llama a la clase padre y se limita la entrada de datos a dos
        Calculadora.__init__(self,2)
    
    def suma(self):
        a,b, = self.datos
        s = a + b
        print('Suma {} + {} = {}'.format(a, b, s))
        
    def resta(self):
        a,b, = self.datos
        r = a - b
        print('Resta {} - {} = {}'.format(a, b, r))
        
    def mult(self):
        a,b, = self.datos
        m = a * b
        print('Multiplicación {} * {} = {}'.format(a, b, m))
        
    def div(self):
        a,b, = self.datos
        d = float(a / b)
        print('Resta {} / {} = {}'.format(a, b, round(d,2)))
# Clase hija    
class Raiz(Calculadora):
    def __init__(self):
        # Se llama a la clase padre y se limita la entrada de datos a uno
        Calculadora.__init__(self,1)
        
    def cuadrada(self):
        import math # Permite usar funciones directas a travez de librerias
        a, = self.datos
        print('Raiz {} ^ (1/2) = {}: '.format(a, round(math.sqrt(a),2)))
        
# Ejecutar el código
calculo = int(input('Ingrese el cálculo que desea realizar:\n1. Operaciones Básicas\n2. Raíz\n\n'))

if calculo == 1:
    op_bas = Ope_Basicas()
    print(op_bas.ingresardato())
    op = int(input('Ingrese la operación a realizar:\n1. Suma\n2. Resta\n3. Multiplicación\n4. Division\n\n'))
    if op == 1:
        print(op_bas.suma())
    elif op == 2:
        print(op_bas.resta())
    elif op == 3:
        print(op_bas.mult())
    elif op == 4:
        print(op_bas.div())
elif calculo == 2:
    raiz_cuadrada = Raiz()
    print(raiz_cuadrada.ingresardato())
    print(raiz_cuadrada.cuadrada())