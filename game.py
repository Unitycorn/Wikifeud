from tabulate import tabulate
import article
import audio
from fuzzywuzzy import fuzz
from colorama import init, Fore, Style
init(autoreset=True)
import highscore
#extra feature: import fireworks


def create_board():
    """
    Create an empty 5x4 board
    """
    board = []
    for _ in range(5):
        row = []
        for _ in range(4):
            row.append("")
        board.append(row)
    return board


def print_board(board, headers):
    """
    Print the board using tabulate
    """
    print(tabulate(board, headers=headers, tablefmt="simple_grid"))


def comparation_with_fuzzy(word_player, word_article, threshold = 85):
    """
        Compares a given word from a player against a list of words from an article
        using fuzzy string matching.

        Args:
            word_player (str): The word provided by the player.
            word_article (list of str): A list of words extracted from an article.
            threshold (int, optional): The minimum fuzzy ratio (percentage) required
                                        for a match. Defaults to 85.

        Returns:
            bool: True if any word in the article has a fuzzy ratio greater than or
                  equal to the threshold with the player's word, False otherwise.
                  The comparison is case-insensitive.
        """
    for word in word_article:
        if fuzz.ratio(word_player.lower(), word.lower()) >= threshold:
            return True
    return False


def get_unfuzzed_word_from_dictionary(word_player, word_article, threshold = 85):
    """
        Attempts to find a word in the article's word list that has a high fuzzy
        similarity to the player's word.

        Args:
            word_player (str): The word provided by the player.
            word_article (list of str): A list of words extracted from an article.
            threshold (int, optional): The minimum fuzzy ratio (percentage) required
                                        for a match. Defaults to 85.

        Returns:
            str: If a word in the article has a fuzzy ratio greater than or equal to
                 the threshold with the player's word, that word from the article
                 is returned. Otherwise, the original player's word is returned.
                 The comparison is case-insensitive.
        """
    for word in word_article:
        if fuzz.ratio(word_player.lower(), word.lower()) >= threshold:
            return word
    return word_player


def play_game(ordered_players):
    """
        Initializes and sets up the game environment for a round.

        Args:
            ordered_players (list of str): A list of player names in the order they
                                           will take turns.

        Returns:
            tuple: A tuple containing:
                - dict: A dictionary to store each player's score, initialized to 0.
                - list: A cleaned list of words extracted from the chosen Wikipedia article.
                - dict: A dictionary containing the frequency of each word in the article.
                - str: The text content of the chosen Wikipedia article.
                - str: The title of the chosen Wikipedia article.
        """
    wiki_text, wiki_title = article.set_topic()
    list_of_words = article.text_to_clean_list(wiki_text)
    wiki_top_words_dict = article.words_frequency(list_of_words)
    user_scores = {}

    for player in ordered_players:
        user_scores[player] = 0

    print(Fore.CYAN + f"\n{ordered_players[0]} fängt an\n")

    board = create_board()
    headers = [ordered_players[0], "Punkte", ordered_players[1], "Punkte"]

    # print (empty) start board
    print(f"THEMA: {wiki_title}")
    print_board(board, headers)

    for row in range(5):
        """
        diese Funktion lässt den ersten Spieler in der Liste für fünf Runden spielen,
        wobei er Wörter eingibt, die mit den häufigsten Wörtern eines Artikels verglichen werden
        """
        # Player 1
        player_1 = ordered_players[0]
        word_1 = input(f"{player_1}, gib dein Wort ein: ").capitalize()
        if comparation_with_fuzzy(word_1, wiki_top_words_dict) and word_1 not in wiki_title:
            fuzzed_word = get_unfuzzed_word_from_dictionary(word_1, wiki_top_words_dict)
            board[row][0] = fuzzed_word
            board[row][1] = wiki_top_words_dict[fuzzed_word]
            user_scores[player_1] += wiki_top_words_dict[fuzzed_word]
        else:
            board[row][0] = word_1
            board[row][1] = 0
            print(Fore.RED + "Dieses Wort ist nicht in der Liste.")

        # print updated board
        print(f"THEMA: {wiki_title}")
        print_board(board, headers)

        # Player 2
        player_2 = ordered_players[1]
        word_2 = input(f"{player_2}, gib dein Wort ein: ").capitalize()

        if comparation_with_fuzzy(word_2, wiki_top_words_dict) and word_2 not in wiki_title:
            fuzzed_word = get_unfuzzed_word_from_dictionary(word_2, wiki_top_words_dict)
            board[row][2] = fuzzed_word
            board[row][3] = wiki_top_words_dict[fuzzed_word]
            user_scores[player_2] += wiki_top_words_dict[fuzzed_word]
        else:
            board[row][2] = word_2
            board[row][3] = 0
            print(Fore.RED + "Dieses Wort ist nicht in der Liste.")

        # print updated board
        print(f"THEMA: {wiki_title}")
        print_board(board, headers)

    # print final board
    print(f"THEMA: {wiki_title}")
    print_board(board, headers)
    return user_scores, wiki_title


def print_winner(user_scores, title):
    """
        This function prints the game results and the winner to the console.
                  It also triggers the playback of a victory audio.
        Args:
            user_scores (dict): A dictionary where keys are player names (str) and
                                values are their corresponding scores (int).
    """
    #ruft punktestand ab
    player1 = {'name': "", 'score': 0}
    player2 = {'name': "", 'score': 0}
    player1['name'], player2['name'] = user_scores.keys()
    player1['score'], player2['score'] = user_scores.values()
    audio.play_music("audio/victory.mp3")

    #gibt den gewinner bekannt
    print(Fore.MAGENTA + "------- Spielende -------")
    print(Fore.CYAN + f"{player1["name"]} hat {player1["score"]} Punkte.")
    print(Fore.CYAN + f"{player2["name"]} hat {player2["score"]} Punkte.")

    if player1["score"] > player2["score"]:
        print(Fore.MAGENTA + f"Gewinner: {player1 ["name"]}! Herzlichen Glückwunsch!")
        print_winner_graphic()

    elif player2["score"] > player1["score"]:
        print(Fore.MAGENTA + f"Gewinner: {player2 ["name"]}! Herzlichen Glückwunsch! ")
        print_winner_graphic()

    else:
        print(Fore.YELLOW + "Unentschieden! Beide Spieler haben gleich viele Punkte.")

    # zeige die Infos zum Wiki-Artikel an & update die highscore-datei
    article.print_wiki_summary(title)
    input(Fore.MAGENTA + "\nDrücke enter, um das Hauptmenü anzuzeigen.")
    highscore.update_highscore_file(player1, player2)


def print_winner_graphic():
    winner_art = [
        "                    ██     ██ ██ ███    ██ ███    ██ ███████ ██████  ",
        "                    ██     ██ ██ ████   ██ ████   ██ ██      ██   ██ ",
        "                    ██  █  ██ ██ ██ ██  ██ ██ ██  ██ █████   ██████  ",
        "                    ██ ███ ██ ██ ██  ██ ██ ██  ██ ██ ██      ██   ██ ",
        "                     ███ ███  ██ ██   ████ ██   ████ ███████ ██   ██ "]

    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

    for i, line in enumerate(winner_art):
        color = colors[i % len(colors)]
        print(color + Style.BRIGHT + line + Style.RESET_ALL)

    # fireworks.full_fireworks()