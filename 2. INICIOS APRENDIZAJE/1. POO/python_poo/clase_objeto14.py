# Clase y estático

class Pastel:
    # Creacion del constructor y sus atributos
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes
    
    # Comprende lo que deseamos hacer con el compilador
    def __repr__(self):
        return f'pastel({self.ingredientes !r})'    
    
    # Método de clase, hacemos independiente todo lo del método
    @classmethod
    def Pastel_chocolate(cls):
        # Trabajamos con diferentes datos para ingredientes y que van a pertenecer a esta clase
        return cls(['Harina', 'Leche', 'Chocolate'])
    
    # Método de clase, hacemos independiente todo lo del método
    @classmethod
    def Pastel_vainilla(cls):
        # Trabajamos con diferentes datos para ingredientes y que van a pertenecer a esta clase
        return cls(['Harina', 'Leche', 'Vainilla', 'Huevos'])
    
print(Pastel.Pastel_chocolate())
print(Pastel.Pastel_vainilla())
    