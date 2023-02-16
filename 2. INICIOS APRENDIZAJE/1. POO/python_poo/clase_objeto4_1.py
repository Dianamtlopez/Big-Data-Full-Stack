class Matematica:
    #Creacion de métodos
    #self hace referencia a un determinado objeto
    def suma(self, n1, n2):
        self.n1 = 0
        self.n2 = 0
        n3 = n1 + n2
        return n3

# Creacion del objeto para acceder al método
s = Matematica()

a = int(input("Ingrese un valor entero: "))
b = int(input("Ingrese otro valor entero: "))

# Llamado del método
sum = s.suma(a,b)

# Impresión del resultado
print(sum)