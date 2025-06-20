import rules
import user
import audio
import game
import highscore
from colorama import Fore, Back, Style, init
init(autoreset=True)


def print_welcome_menu():
    print(Fore.YELLOW + Style.BRIGHT + "                    ********** Wiki Feud **********")

    print(Fore.CYAN + Style.BRIGHT + r"""  
                                           ______                     ||
                \ \      / (_) | | / /(_) |  ___|  _    _    _   _____||
                 \ \ /\ / /| | | |/ / | | |  |_  // \\ | |  | | ||----||
                  \ V  V / | | | |\ \ | | |  _| ||__// | |__| | ||____||
                   \_/\_/  |_| |_| \ \|_| |_|   ||___  |______| ||____||""")
    print()
    print(Fore.YELLOW + Style.BRIGHT + "                    *** by Task Force None © ***")
    print()
    print("                         [1] Neues Spiel")
    print("                         [2] Spielregeln")
    print("                         [3] Bestenliste")
    print("                         [4] Credits")
    print("                         [5] Beenden")
    print()

def main():
    """
   play title melody of family feud, greet user and get user choice from the menu
    """
    audio.play_music("audio/family_feud.mp3")

    while True:
        print_welcome_menu()
        auswahl = input(Fore.YELLOW + "Bitte wähle eine Option (1-5): ")

        if auswahl == "1":
            ordered_players = (user.get_order_of_players(user.get_name_of_players()))
            user_scores, title = game.play_game(ordered_players)
            game.print_winner(user_scores, title)
        elif auswahl == "2":
            rules.print_game_rules()
        elif auswahl == "3":
            highscore.print_highscores()
        elif auswahl == "4":
            rules.print_credits()
        elif auswahl == "5":
            print(Fore.CYAN + "\nAuf Wiedersehen")
            break
        else:
            print(Fore.RED + "Falsche Eingabe ")


if __name__ == "__main__":
    main()