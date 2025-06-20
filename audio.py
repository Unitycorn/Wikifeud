from threading import Thread
from playsound import playsound

# pip3 install playsound
# pip3 install PyObjC

def play_music(path):
    """
    Plays selected sound file in separate thread so it doesn't block the main program
    """
    def play_thread_function():
        playsound(path)

    play_thread = Thread(target=play_thread_function)
    play_thread.start()
