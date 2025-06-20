import wikipedia
import spacy
import warnings
from bs4 import GuessedAtParserWarning
warnings.filterwarnings('ignore', category=GuessedAtParserWarning)
from colorama import init, Fore, Style
init(autoreset=True)
import textwrap


def text_to_clean_list(wiki_text):
    """
    Takes any text (string) and cleanses it from punctuation and extracts the nouns via spacy.
    :param wiki_text:
    :return: clean list of nouns
    """
    print(Fore.YELLOW + "\nDaten werden verarbeitet und die Wortliste generiert...")
    nlp = spacy.load("de_dep_news_trf")
    doc = nlp(wiki_text)
    list_of_words = []
    for token in doc:
        if token.pos_ == "NOUN" or token.pos_ == "PROPN":
            list_of_words.append(token.text)
    return list_of_words


def words_frequency(words):
    """
    Takes a list of nouns and creates a dictionary that maps nouns to their frequency.
    :param words:
    :return: frequency_dictionary
    """
    frequency_dict = {}
    for word in words:
        if len(word) > 1:
            if word not in frequency_dict:
                frequency_dict[word] = 1
            else:
                frequency_dict[word] += 1
    return frequency_dict


def set_topic():
    """
    Selects a random page title from wikipedia and checks for a specific length
    to have a reasonable amount of words. If the content is too short, we look for another.

    :return: the wiki content (string)
    """
    print(Fore.BLUE + "\nBitte warten... Thema wird geladen...")
    wikipedia.set_lang("de")

    while True:
        try:
            random_title = wikipedia.random(pages=1)
            random_page = wikipedia.page(random_title, auto_suggest=False)
        except wikipedia.exceptions.DisambiguationError:
            continue
        except wikipedia.exceptions.PageError:
            continue
        random_content = random_page.content
        words = random_content.split(" ")
        word_list = list(words)
        if len(word_list) >= 900:
            print(Fore.CYAN + f"\nDas Thema für diese Runde: {random_title}")
            selection = input("Wähle [1] um Thema zu wählen, drücke [2] um ein neues Thema zu generieren:\n")
            if selection == '1':
                return random_content, random_title
            if selection == '2':
                print(Fore.CYAN + "\nBitte warten... Thema wird geladen....")
                continue


def print_wiki_summary(title):
    """
    inform players about the background of their chosen topic
    and offer outgoing wiki-link for further information
    """
    wiki_page = wikipedia.page(title, auto_suggest = False)
    content = wiki_page.summary
    wrapped_content = textwrap.fill(content, width=100)
    print(f"\nHier ist die Zusammenfassung des Artikels zu {title}:\n")
    print(wrapped_content)
    print("\nVollständiger Artikel unter:\n")
    url_string = generate_wiki_url_from_title(title)
    print(f"https://de.wikipedia.org/wiki/{url_string}\n")


def generate_wiki_url_from_title(title):
    """
    takes title of wikipedia page and generates wikipedia page url
    by replacing (ä,Ä,ö,Ö,ü,Ü,ß and spaces)
    """
    url_string = title.replace(" ", "_")
    url_string = url_string.replace("ä", "%C3%A4")
    url_string = url_string.replace("Ä", "%C3%84")
    url_string = url_string.replace("ö", "%C3%B6")
    url_string = url_string.replace("Ö", "%C3%96")
    url_string = url_string.replace("ü", "%C3%BC")
    url_string = url_string.replace("Ü", "%C3%9C")
    url_string = url_string.replace("ß", "%C3%9F")
    return url_string


