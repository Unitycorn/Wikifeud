import random
from colorama import Fore

def get_name_of_players():
    """
    Get the name of the two players, put them into a list and returns the list
    """
    players_list = []
    for i in range(2):
        while True:
            name = (input(Fore.YELLOW + f"Gib den Namen für Spieler {i + 1} ein: "))
            if name == "":
                print(Fore.RED + "Der Name darf nicht leer sein :)")
            else:
                players_list.append(name)
                break
    return players_list


def get_order_of_players(players_list):
    """
    Randomly selects the first player and returns players in order
    """
    first = random.choice(players_list)
    if players_list[0] == first:
        second = players_list[1]
    else:
        second = players_list[0]
    ordered_list = [first, second]
    return ordered_list

