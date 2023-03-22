#***************************************************************************************************************
#* VERSION FINAL matrix_process                                                                                *
#* Presentado por DIANA MARIA TORO LOPEZ                                                                       *
#***************************************************************************************************************



from functools import reduce

def process_matrix (matrix, rows, columns):
    """
        Recibe una matríz de números y devuelve una nueva con los elementos cambiados, cada elemento
        de la nueva, será el promedio del valor antiguo de cada casilla y el de sus vecinos, sin promediar
        las casillas que dan con el borde de la matríz
    """
    processed_matrix = []
    # Si la matríz es de 1x1, nos va a devolver la misma matríz.
    # Aunque ya esté evaluado en el main, veo obligatorio dejar estas validaciones, en el caso de que
    # vaya a ser usada la función sin el main().
    if rows == 0 and columns == 0:
        processed_matrix = matrix
        print(f'La matríz está vacía: {matrix}')
    elif rows == 1 and columns == 1:
        processed_matrix = matrix
        print(f'La matríz tiene un elemento: {matrix}')
    else:
        # para las matrices m x n > 1.
        # Bucle para extraer los índices de la matríz, este proceso se realizará para obtener una idea
        # visual de los índices, en esté ejercicio, esta matríz, no será utilizada en los procedimientos.
        for r in range(rows):
            list_index = []
            for c in range(columns):
                list_index.append(matrix.index(matrix[r]))
            processed_matrix.append(list_index)
            
        print('\nNueva matríz creada con los índices de la matríz inicial: \n')
        # Bucle para visualizar la matríz de índices, en este caso solo es visual para entender la posición.
        # de los índices y/o valores de la matríz
        for r in range(rows):
            for c in range(columns):
                print([r,c], end=' ')
            print()
        # Se instancia el objeto new_element, por medio del llamado a la función process_element,
        # enviando por argumento matrix, filas, columnas 
        new_element = process_element(matrix, rows, columns)
    
    return processed_matrix

def process_element(matrix, rows, columns):
    """
        Recibe la matríz, junto con sus filas y sus columnas, se procesa y se convierte en una matriz
        con sus bordes iguales, pero en su interior se promedia acorde al requerimiento inicial.
    """
    # Se instancia el objeto matrix_neighbours, por medio del llamado a la función get_neighbour_values,
    # enviando por argumento matrix, filas, columnas.
    matrix_neighbours = get_neighbour_values(matrix, rows, columns)
    # Se instancia el objeto matrix_neighbours, por medio del llamado a la función get_average,
    # enviando por argumento matrix_neighbours, filas, columnas.
    average = get_average(matrix_neighbours, rows, columns)
    # se retorna a la 

# Obtener valores de vecinos
def get_neighbour_values(matrix, rows, columns):
    """
        Devuelve una matríz, cuyos elementos son:
        esquinas: contiene tres valores, el propio, el vecino del lado y el de abajo o arriba según el caso.
        bordes: contiene 4 valores, el propio, los dos vecinos de los lados y el de abajo o arriba según el caso.
        parte interna de la matríz inicial: contiene 5 valores, el propio, slos dos vecinos de los extremos y los
        vecinos de arriba y abajo.
    """
    
    matrix_neighbours = []
    for r in range(rows):
        list_aux = []
        for c in range(columns):
            aux = []
            aux1 = 0
            # Este condicional es fundamental para poder lograr la organizacion de los bordes
            # y que me deje trabajar con la parte interna
            if r == 0 and c == 0 :
                aux.append(matrix[r][c])
                aux.append(matrix[r][c+1])
                aux.append(matrix[r+1][c])
                list_aux.append(aux)
                # list_aux.append(None)
            elif r == 0 and c == columns-1:
                aux.append(matrix[r][c])
                aux.append(matrix[r][c-1])
                aux.append(matrix[r+1][c])
                list_aux.append(aux)
                # list_aux.append(None)
            elif r == rows-1 and c == 0:
                aux.append(matrix[r][c])
                aux.append(matrix[r][c+1])
                aux.append(matrix[r-1][c])
                list_aux.append(aux)
                # list_aux.append(None)
            elif r == rows-1 and c == columns-1:
                aux.append(matrix[r][c])
                aux.append(matrix[r][c-1])
                aux.append(matrix[r-1][c])
                list_aux.append(aux)
                # list_aux.append(None
            elif r == 0:
                aux.append(matrix[r][c])
                aux.append(matrix[r][c-1])
                aux.append(matrix[r][c+1])
                aux.append(matrix[r+1][c])
                list_aux.append(aux)
                # list_aux.append(None)
            elif c == 0:
                aux.append(matrix[r][c])
                aux.append(matrix[r+1][c])
                aux.append(matrix[r-1][c])
                aux.append(matrix[r][c+1])
                list_aux.append(aux)
                # list_aux.append(None
            elif r == rows-1:
                aux.append(matrix[r][c])
                aux.append(matrix[r][c-1])
                aux.append(matrix[r][c+1])
                aux.append(matrix[r-1][c])
                list_aux.append(aux)
                # list_aux.append(None)
            elif c == columns-1:
                aux.append(matrix[r][c])
                aux.append(matrix[r+1][c])
                aux.append(matrix[r-1][c])
                aux.append(matrix[r][c-1])
                list_aux.append(aux)
                # list_aux.append(None)
            else:
                # Al aislar la primera y ultima posición de las filas y la primera y ultima posición de las columnas,
                # he logrado tener en cuenta solo los numeros internos para alcanzar el resultado
                aux.append(matrix[r][c])
                aux.append(matrix[r][c+1])
                aux.append(matrix[r][c-1])
                aux.append(matrix[r-1][c])
                aux.append(matrix[r+1][c])
                # Se adicionan los elementos x filas a la list_aux.
                list_aux.append(aux)
        # Se adiciona la list_aux que me representa cada fila en la matríz.
        matrix_neighbours.append(list_aux)
    
    # Bucle para visualizar la matríz. 
    print('\nNueva matríz creada con los vecinos de cada elemento de la matríz inicial: \n')
    for r in range(rows):
        for c in range(columns):
            print(matrix_neighbours[r][c], end=' ')
        print()
        
    return matrix_neighbours

def get_average(matrix_neighbours, rows, columns):
    """
        Recibe una matríz que en sus bordes cuenta con los numeros iniciales de la matríz y en su parte interna
        tiene los vecinos en forma de cruz de cada elemento, incluido el elemento y devuelve una matríz con el
        borde igual y en su parte interna los promedios de los vecinos 
    """
    # este valor siempre va a ser constante ya que los vecinos son los mismos dependiendo el caso
    cantidad_internos = 5
    cantidad_esquinas = 3
    cantidad_bordes = 4
    
    matrix_promedio = []
    for r in range(rows):
        list_aux = []
        for c in range(columns):
            aux = 0
            # Este condicional es fundamental para poder lograr la organizacion de los bordes
            # y que me deje trabajar con la parte interna
            # Esquina superior izquierda
            if r == 0 and c == 0 :
                aux = reduce(lambda accum,b: accum + b, matrix_neighbours[r][c], 0) / cantidad_esquinas
                # Se usa round para darle forma estética a la matriz
                list_aux.append(round(aux,2))
                # list_aux.append(None)
            # Esquina inferior derecha
            elif r == 0 and c == columns-1:
                aux = reduce(lambda accum,b: accum + b, matrix_neighbours[r][c], 0) / cantidad_esquinas
                # Se usa round para darle forma estética a la matriz
                list_aux.append(round(aux,2))
                # list_aux.append(None)
            # Esquina Inferior Izquierda
            elif r == rows-1 and c == 0:
                aux = reduce(lambda accum,b: accum + b, matrix_neighbours[r][c], 0) / cantidad_esquinas
                # Se usa round para darle forma estética a la matriz
                list_aux.append(round(aux,2))
                # list_aux.append(None)
            # Esquina inferior derecha
            elif r == rows-1 and c == columns-1:
                aux = reduce(lambda accum,b: accum + b, matrix_neighbours[r][c], 0) / cantidad_esquinas
                # Se usa round para darle forma estética a la matriz
                list_aux.append(round(aux,2))
                # list_aux.append(None 
            elif r == 0:
                aux = reduce(lambda accum,b: accum + b, matrix_neighbours[r][c], 0) / cantidad_bordes
                # Se usa round para darle forma estética a la matriz
                list_aux.append(round(aux,2))
                # list_aux.append(None)
            elif c == 0:
                aux = reduce(lambda accum,b: accum + b, matrix_neighbours[r][c], 0) / cantidad_bordes
                list_aux.append(round(aux,2))
                # list_aux.append(None
            elif r == rows-1:
                aux = reduce(lambda accum,b: accum + b, matrix_neighbours[r][c], 0) / cantidad_bordes
                # Se usa round para darle forma estética a la matriz
                list_aux.append(round(aux,2))
                # list_aux.append(None)
            elif c == columns-1:
                aux = reduce(lambda accum,b: accum + b, matrix_neighbours[r][c], 0) / cantidad_bordes
                # Se usa round para darle forma estética a la matriz
                list_aux.append(round(aux,2))
                # list_aux.append(None)
            else:
                # Se sacan los promedios de los valores internos.
                aux = reduce(lambda accum,b: accum + b, matrix_neighbours[r][c], 0) / cantidad_internos
                # Se adicionan estos promedios a la list_aux.
                list_aux.append(round(aux,2))
        # se adiciona la list_aux a la matríz "matrix_promedio"
        matrix_promedio.append(list_aux)
    print('\nNueva matríz creada con los promedios de los vecinos de cada elemento de la matríz inicial: \n')
    # Bucle para visualizar la matríz
    for r in range(rows):
        for c in range(columns):
            print(matrix_promedio[r][c], end=' ')
        print()     
    return matrix_neighbours
            
# Finción de maximo Nivel.
def main():
    """
        «Código de máximo nivel» es el primer módulo de Python especificado por el usuario que empieza a ejecutarse.
        Es «de máximo nivel» porque importa todos los demás módulos que necesita el programa.
    """
    # Se genera la matríz inicial de m x n en este caso es 6 x 6, pudiendose crear de mayor tamaño,
    # siempre y cuando sea simétricamente cuadrada.
    size = int(input("Matriz M X N, ingresa el valor para el tamaño de la matríz: "))    
    matrix = []
    for r in range(size):
        list_aux = []
        for c in range(size):
            # Se almacena cada fila en una list_aux.
            list_aux.append(1+c)
        #Se almacena cada fila en la matríz.
        matrix.append(list_aux)
    
    if size == 0:
        # Evalúa si la patriz está vacçía
        print(f'La matríz está vacía: {matrix}')
    elif size == 1:
        # Evalúa si la matriz tiene un elemento
        print(f'La matríz tiene un elemento: {matrix}')
    else:
        # Bucle para visualizar la matríz.
        print(f'\nSe ha generdo la siguiente matríz {size} X {size}: \n')
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                print(matrix[r][c], end=' ')
            print()
    
        # se hace el llamado a la funcion process:matrix.
        process_matrix(matrix, len(matrix), len(matrix[0]))

# Se ejecuta el main.   
main()