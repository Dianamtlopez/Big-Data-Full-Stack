from play import *

def run_game():
    """Arranca el juego"""
    display_game()
    # cual es la jugada del usuario
    user_play = get_user_play()
    # Jugada del ordenador
    comp_play = random_play()
    # ?
    display_match(user_play, comp_play)
    # determinar quien es el ganador
    winner = get_winner(user_play, comp_play)
    # si es empate
    if winner == None:
        # muestra empate
        display_tie(user_play, comp_play)
    else:
        # muestro el resultado
        display_victory(winner)

def display_match(play1, play2):
    print(f'{play1.description()} vs {play2.description()}    FIGHT!\n')

def display_game():
    # muestra el nombre del juego
    print('Rock Paper Scissors')
    
def get_user_play():
    """
        Le pregunta al usuario que quiere jugar y lo devuelve
    """
    res = get_user_response()
    if res == 1:
        return Rock()
    elif res == 2:
        return Paper()
    else:
        return Scissors()

def get_user_response():    
    """
        presenta un menú de opciones y pide que selecciones una.
        Devuelve una cadena que indica lo que ha elegido
    """
    # siempre tiene una condicion booleana que mientras sea verdad será un bucle infinito
    response = None
    while True:
        print("Choise your play: ")
        print("1. Rock")
        print("1. Paper")
        print("1. Scissors")
        raw = input("Enter 1, 2 or 3:\n")
        # validar raw
        raw = raw.strip()
        if raw == '1': 
            response = 1
            break
        elif raw == '2': 
            response = 2
            break
        elif raw == '3': 
            response = 3
            break
        else:
            continue
    return response

def random_play():
    #Selecciona una jugada al azar para competir con el usuario
    # me devuelve una instancia de las clases
    return choice([Paper(), Rock(), Scissors()])

def get_winner(play1, play2):
    #Obtiene el vencedor o None si hay empate
    return play1

def display_tie(play1, play2):
    # Imprime que ha habido un empate
    print(f'Empate entre dos {play1.description()}')

def display_victory(winner):
    # Muestra que winner ha ganado
    print(f'Ha ganado {winner.description()}')

# es la manera de decir que aqui inicia el programa
if __name__ == '__main__':
    run_game()

game = run_game()
print(game)