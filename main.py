from pytube.exceptions import RegexMatchError
from pytube.helpers import regex_search
from src.tela import telaa as tela
from src.down import down as dw
import time

def inicio():
    try:
        tela.menu()
        if input() == 'p':
            while True:
                try:
                    down = dw()
                    link = tela.playlist()
                    down.tipo('p', link)
                    title = down.nome()
                    if tela.downConfirm(title):
                        down.down()
                    break
                except KeyboardInterrupt:
                    break
                except RegexMatchError:
                    print("Link inválido")
                    time.sleep(2)
                finally:
                    inicio()
        else:
            while True:
                try:
                    down = dw()
                    link = tela.video()
                    down.tipo('v', link)
                    title = down.nome()
                    if tela.downConfirm(title):
                        down.down()
                    break
                except KeyboardInterrupt:
                    break
                except RegexMatchError:
                    print("Link inválido")
                    time.sleep(2)
                finally:
                    inicio()
    except KeyboardInterrupt:
        tela.clearScreen()

def ini():
    try:
        tela.telaini()
    except KeyboardInterrupt:
        tela.clearScreen()
    else:
        inicio()

if __name__ == '__main__':
    ini()
