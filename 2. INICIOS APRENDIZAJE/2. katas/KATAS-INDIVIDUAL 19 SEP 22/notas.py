# f-strings

class Estudiante:
    # Constructor
    def __init__(self,cant_est):
        self.cant_est = cant_est
        
        # Creacion de las listas para almacenar los datos
        self.nombre = [0 for i in range(cant_est)]
        self.apellido = [0 for i in range(cant_est)]
        self.asignatura_eva = [0 for i in range(cant_est)]
        self.nota = [0 for i in range(cant_est)]
        self.estado = [0 for i in range(cant_est)]
    
    # método
    def capturar_datos(self):
        # Captura de datos
        if self.cant_est > 0:
            self.asignatura = input("Ingrese la asignatura evaluada: ")
            i = 0
            while i < self.cant_est:
                self.nombre.append(input(f"Ingrese el nombre del estudiante No {i+1}: "))
                self.apellido.append(input(f"Ingrese el apellido del estudiante No {i+1}: "))
                self.asignatura_eva.append(self.asignatura)
                self.nota.append(float(input(f"Ingrese la nota del estudiante No {i+1}: ")))
                print("\n")
                i += 1
    
    # método
    def resultado(self):
        # Para el iterador La primera posicion es ceros y se incrementan estos ceros de acuerdo a la variable cant_est
        i = self.cant_est
        for pos in self.nota[i:]:
            if pos >= 0 and pos < 6:
                self.estado.append('Reprobó')
            else:
                self.estado.append('Aprobó')
            i += 1
    
    # método
    def imprimir(self):
        # Para el iterador La primera posicion es ceros y se incrementan estos ceros de acuerdo a la variable cant_est
        i = self.cant_est
        # se crea un miniformato para mistrar los datos
        sep = '---------------------------------------------------------------------------------------------'
        print('{0}\n\tNOMBRE\t\tAPELLIDO\tASIGNATURA\t\tNOTA\t\tESTADO\n{0}'.format(sep))
        for nomb, ape, asig, nota, est in (zip(self.nombre[i:], self.apellido[i:], self.asignatura_eva[i:], self.nota[i:], self.estado[i:])):
            print(f'\t{nomb}\t\t{ape}\t\t{asig}\t\t\t{nota}\t\t{est}\n{sep}')
        
c_e = int(input("Ingrese la cantidad de estudiantes que desea almacenar: "))
# se crea el objeto y se le envía la cantidad de estudiantes por argumento
nota_final = Estudiante(c_e)
# Se hace llamado a los métodos para su ejecución
nota_final.capturar_datos()
nota_final.resultado()
nota_final.imprimir()
