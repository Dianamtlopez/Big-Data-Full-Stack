from procesado_lista import process_list
numbers = [1,2,3,4,5,6,7,8,9,10]

if __name__ == "__main__":
    averages = process_list(numbers)
    print(numbers)
    print('Averages')
    tamaño = len(averages)-2
    averages.pop(0)
    averages.pop(tamaño)
    print(averages)

"""    
    for i in range(10):
        averages = process_list(averages)
        print(averages)
"""