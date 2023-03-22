from functools import reduce

def process_list(elements):
    # el interno que tiene dos cecino
    # esté el primero y el ultimo
    """
        Recibe una lista de números y devuelve una nueva con los elementos cambiados, cada elemento
        de la nueva, será el promedio del valor antiguo y el de sus vecinos
    """
    processed_list = []
    if len(elements) == 1:
        processed_list = elements
    else:
        # por cada elemento de la lista....
        for index, element in enumerate(elements):
            # lo proceso 
            new_element = process_element(index, elements)
            # lo añado a la lista
            processed_list.append(new_element)
    # devuelvo la nueva lista
    return processed_list

def process_element(index, elements):
    """
        Recibe el indice de un elemento y la lista en la que está,
        calcula su promedio con sus vecinos y devuelve dicho promedio.
    """
    # obtengo la lista de vecinos incluido el elemento
    indices = get_neighbour_indices(index, elements)
    values = get_neighbour_values(indices, elements)
    # calculo su promedio
    average = get_average(values)
    # se asigna el primero y el ultimo elemento en una nueva lista
    return average

# Obtener vecinos
def get_neighbour_indices(index, elements):
   # Devuelve la lista de indices de los vecinos, se incluye al propio elemento
    indices_old = []
    indices = []
    # index == 0
    if index == 0:
        # el primero
        indices.append(index + 1)
    if index == len(elements) - 1:
        # es ultimo
        indices.append(index - 1)
    else:
        # indices del medio
        indices.append(index + 1)
        indices.append(index - 1)
    
    # incluyo al principio el elemento como vecino de si mismo
    indices.append(index)
    
    #indices_old.append(index)
    
    # elimino los indices imposibles (menores que cero y mayores o iguales a la
    # longitud de la lista)
    # deberes hacer un filter a indices para eliminar valores imposible -0 y >= len(lista)
    #indices = list(filter(lambda x: x > 0 and x <= len(indices1), indices1))
    return indices

def get_neighbour_values(indices, elements):
    # obtengo la lista de vecinos
    values = []
    for index in indices:
        values.append(elements[index])
    return values

# Promedio
def get_average(values):
    """
        Recibe una lista de numeros y devuelve su promedio
    """
    return reduce(lambda accum,b: accum + b, values, 0) / len(values)
