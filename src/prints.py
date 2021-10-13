import os
from src.downs import *

def home_screen():
    clean_screen()
    print('''
    O que deseja baixar?

    1 - Video
    2 - Playlist
    ''')
    optionDown = int(input())
    if optionDown == 1:
        video()
    else:
        playlist()

def clean_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def down_concluded(tipo):
    print(f'''
    O que deseja agora?

    1 - Baixar outro {tipo}
    2 - Menu inicial
    ''')
    option = int(input())
    if option == 1:
        video()
    else:
        home_screen()