class Coin():
    def __init__(self, moneda):
        self.moneda = moneda

class Booleans():
    def __init__(self, boolen):
        self.boolen = boolen     

def sum_all(numbers):
    """
        Recibe una lista de numeros y los combina (mediante +) a uno solo, que será el total
    """
    total_so_far = 0
    for element in numbers:
        total_so_far = total_so_far + element
    return total_so_far

def mul_all(numbers):
    """
        Recibe una lista de numeros y los combina (mediante *) a uno solo, que será el total
    """
    total_so_far = 1
    for element in numbers:
        total_so_far = total_so_far * element
    return total_so_far

def and_all(booleans):
    """
        Recibe una lista de numeros y los combina (mediante and) a uno solo, que será el total
    """
    total_so_far = True
    for element in booleans:
        total_so_far = total_so_far * element
    return total_so_far

def String_all(strings):
    """
        Recibe una lista de numeros y los combina (mediante +) a uno solo, que será el total
    """
    total_so_far = True
    for element in strings:
        total_so_far = total_so_far + element
    return total_so_far

lista = [1,2,3,4,5]
resultado = mul_all(lista)
print(resultado)

