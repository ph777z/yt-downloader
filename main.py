from pytube.helpers import regex_search
from src.tela import tela
from src.down import down
import time

down = down()
tela = tela()

def inicio():
    try:
        tela.menu()
        if input() == 'p':
            while True:
                link = tela.playlist()
                try:
                    down.tipo('p', link)
                    title = down.nome()
                    if tela.downConfirm(title):
                        down.down()
                    break
                except KeyboardInterrupt:
                    raise KeyboardInterrupt
                """ except:
                    print("Link inválido")
                    time.sleep(2) """
        else:
            while True:
                link = tela.video()
                try:
                    down.tipo('v', link)
                    title = down.nome()
                    if tela.downConfirm(title):
                        down.down()
                    break
                except KeyboardInterrupt:
                    raise KeyboardInterrupt
                """ except:
                    print("Link inválido")
                    time.sleep(2) """
    except KeyboardInterrupt:
        tela.clearScreen()
if __name__ == '__main__':
    inicio()
