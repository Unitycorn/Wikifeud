import json
import pathlib
from colorama import Fore, Style, init
init(autoreset=True)

FILENAME = 'bestenliste.json'


def create_highscore_file():
    """
        Creates a JSON file to store high scores if it doesn't already exist.
        The file, named by the global constant FILENAME, will be created with
        a basic JSON structure containing an empty list under the key "scores".
        If the file already exists, this function does nothing.
        """
    if pathlib.Path(FILENAME).exists():
        pass
    else:
        pass
        # lege json file mit leerer liste an:
        with open(FILENAME, 'w') as datei:
            json.dump({"scores": []}, datei)


def update_highscore_file(player1, player2):
    with open(FILENAME, "r") as file:
        data = json.load(file)

    # Neue Dictionaries zur Liste "scores" hinzufügen
    data["scores"].append(player1)
    data["scores"].append(player2)

    # speichert datei mit neuen und alten daten
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

    print(Fore.GREEN + Style.BRIGHT + f"Die Bestenliste wurde in {FILENAME} gespeichert.")


def print_highscores():
    #zeigt die liste aller bisherigen spielerinnen, geordnet nach den all-time highscores
    with open(FILENAME, 'r', encoding='utf-8') as datei:
        daten = json.load(datei)
    highscores = daten['scores']
    bestenliste_sorted = sorted(highscores, key=lambda d: d['score'], reverse=True)
    print()
    print(Fore.GREEN + "=" * 15)
    print(Fore.GREEN + f"  Highscores:")
    print(Fore.GREEN + "=" * 15)
    for player in bestenliste_sorted:
        print(Fore.CYAN + f"{player['name']} : {player['score']}")
    input(Fore.YELLOW + "\nDrücke [Enter] um zum Menü zurückzukehren")