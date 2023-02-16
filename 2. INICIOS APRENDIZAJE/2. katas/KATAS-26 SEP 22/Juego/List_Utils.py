# Clase List_Utils

# Funciones para:
# Encontrar un elemento en una lista
# encontrar la presencia de n ocurrencias de esos elementos en la lista
# encontrar la presencia de m ocurrencia seguidas en la lista

from platform import python_branch

# Método no usado, solo sirve de Ejemplo
def find_one(list, needle):
    """
        Devuelve True si encuentra a needle en la lista en alguna posición
        Sino, devuelve False
    """
    return find_n(list, needle, 1)

# Método no usado, solo sirve de Ejemplo
def find_n(list, needle, n):
    # Controla que no se ingrese un numero menor o igual a cero
    if n > 0:
        # inicializo el contador de veces que lo he encontrado
        # inicializo el indice del elemento actual
        index = 0
        count = 0
    
        # mientras no haya encontrado n veces y no haya terminado la lista
        while count < n and index < len(list):
            # si la encuentro, actualizo el booleano, el contador y el indice
            if needle == list[index]:
                count += 1
            
            # Pase lo que pase, actualizo el contador
            index += 1
        
        # devuelvo el resultado de comparar n con el contador
        return count >= n, count, index
    else:
        return(f"Dato {n} erroneo!, el valor ingresado debe ser mayor que cero")

# Este método evalúa si se cumple la racha vertical    
def find_streak(list, element, size):
    """
        Devuelve True si en list hay size o más elementos Seguidos
        false en caso contrario y tambien si size es <= 0
    """
    if size > 0:
        # Buscar una racha de 4 de longitud 3: 4, 4, 4
        # Inicializo el indice, el contador y el indicador de racha
        index = 0
        count = 0
        streak = False

        # mientras que no haya encontrado size elementos y la lista no se haya terminado 
        while count < size and index < len(list):
            if list[index] == element:
                # si lo encuentro activo el indicador de rachas e incremento el contador
                streak = True
                count += 1
            else:
              # si no lo encuentro, desactivo el indicador de rachas y pongo contador a cero
                streak = False
                count = 0
            # Avanzo al siguiente elemento (incremento indice)
            index += 1
        # SOLO SI ESTAMOS EN RACHA, devolvemos el resultado de comparar el contador con size
        #if streak == True:
        #    return count >= size
        #else:
        #    return False            

        # otra manera
        # SOLO SI ESTAMOS EN RACHA, devolvemos el resultado de comparar el contador con size
        if streak: return count >= size
    else:
        return False

# Función de prueba, no es utilizada, solo se crea para verificar que si se cumple la labor
def first_elements(list_of_lists, n):
    """ Recibe una matriz (lista de lista) de 4 items y devuelve una lista con los primeros elementos
        de cada una de las listas de la matriz
    """
    # Recibe esto: [[1,2,3,4],[1,2,3,4],[4,3,2,1],[4,3,2,1]]
    # Devuelve esto: [1,1,4,4]
    return nth_elements(list_of_lists, 0)

def nth_elements(list_of_lists, n):
    """ Recibe una matriz (lista de lista) de 4 items y devuelve una lista con los primeros elementos
        de cada una de las listas de la matriz
    """
    # Recibe esto: [[1,2,3,4],[1,2,3,4],[4,3,2,1],[4,3,2,1]]
    # Devuelve esto: [1,1,4,4]
    result = []
    for sub_list in list_of_lists:
        result.append(sub_list[n])
    return result

def transpose(list_of_lists):
    """recibe una matriz y devuelve su transpuesta"""
    # creo una matriz vacía en la que voy acumulando
    transp = []
    # desde cero al ultimo indice de list_oflist
    for index in range(len(list_of_lists)):
        # extraigo sus valores enesimos y se los encasqueto a la acumulada
        transp.append(nth_elements(list_of_lists, index))
    # devuelvo la acumulada
    return transp

def displace(elements, distance):
    """Desplaza una lista distance posiciones a la derecha si distance es positivo
        y a la izquierda si es negarivo"""
    res = elements
    filler = [None] * abs(distance)
    if distance == 0:
        return elements
    elif distance > 0:
        res = filler + res
        return res[:-distance]
    else:
        # distancoa negativa (desplazamos a la izquierda)
        res = res + filler
        return res[abs(distance):]

def displace_matrix(matrix):
    """Des plaza cada una de las listas de la matrix su indice -1"""
    # creouna matriz vacía que iré construyendo
    d = []
    # por cada una columna de la matriz original, la desplazo indice -1
    for i in range(len(matrix)):
        # añado la columna desplazada a la matriz que estoy construyendo
        d.append(displace(matrix[i], i - 1))
    # devuelvo la matriz que he construido
    return d


def replace(elements, predicate, new_value):
    # creamos un acumulador
    new_list = []
    # recorro la lista original
    for element in elements:
        # si un elemento, pasa el test, lo cambio por el nuevo
        if predicate(element):
            new_list.append(new_value)
        # si no, se queda tal cual
        else:
            new_list.append(element)
        # devuelvo el acumulador
        return new_list
    
def replace_matrix(matrix, predicate, new_element):
    accum = []
    for sublist in matrix:
        accum.append(replace(matrix, predicate, new_element))
    return accum


# Para verificar si find_streak funciona
lista = [1, 4, 4, 4, 5, 6]
enc = find_streak(lista,4,3)
print(f'En esta lista enviada: {lista}, ha encontrado una victoria {enc} de 3 elementos.')

# Prueba de funcionamiento
n_lista = [[1,2,3,4],[1,2,3,4],[4,3,2,1],[4,3,2,1]]
print('\nNueva Lista Enviada: [[1,2,3,4],[1,2,3,4],[4,3,2,1],[4,3,2,1]]')
print('con los indices de cada sub lista, se arman las nuevas listas para verificar la transpuesta')
print(nth_elements(n_lista, 0))
print(nth_elements(n_lista, 1))
print(nth_elements(n_lista, 2))
print(nth_elements(n_lista, 3))
print('Se transpone la lista Inicial: [[1,2,3,4],[1,2,3,4],[4,3,2,1],[4,3,2,1]]')
print('Matriz resultado:')
print(transpose(n_lista))
print('Se transpone la lista Transpuesta: [[1,1,4,4],[2,2,3,3],[3,3,2,2],[4,4,1,1]]')
print('Matriz resultado:')
print(transpose(transpose(n_lista)))