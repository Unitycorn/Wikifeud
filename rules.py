from colorama import Fore, Back, Style, init
init(autoreset=True)


def print_game_rules():
    print("\n1. Die Überschrift eines zufälligen Wikipedia Eintrages wird angezeigt.")
    print("2. Jeder Spieler darf abwechselnd fünf mal raten, welches Nomen das häufigste im Wiki-Eintrag ist.")
    print("3. Wer beginnt, wird per Zufall entschieden.")
    print("""4. Die Anzahl der Punkte richtet sich nach der Häufigkeit des Wortes im Wiki-Eintrag 
    (z.B. "Python" kommt 3 mal vor -> 3 Punkte).""")
    print("""5. Jedes Wort ist nur einmal wählbar, hat ein Mitspieler bereits ein Wort geraten, 
    darf dieses nicht erneut benutzt werden""")
    print("6. Sieger ist, wer nach f"
          "ünf erratenen Wörtern die meisten Punkte hat")
    print()
    print(Fore.MAGENTA + "                        - VIEL SPAß -")
    print()
    input(Fore.YELLOW + "'Enter', um ins Hauptmenü zurück zu kehren")


def print_credits():
    print(Fore.YELLOW + "\n** Developed by Task Force None 2025 © All rights reserved **")
    print()
    print("Team :\n\nAnna Pohle \nAline Janke \nAlline Wamsser \nMichael Flaig \nEugen Iwliew \nMarkus Huckriede")
    print("Mit speziellen Dank an 'Ava' und 'Bob' für ihren unermüdlichen Einsatz!")
    print()
    input(Fore.YELLOW + "'Enter', um ins Hauptmenü zurück zu kehren")

