from pytube import YouTube, Playlist, request
from src.tela import tela
import os

tela = tela()
home = os.path.expanduser('~')

class down:
    def __init__(self):
        self.caminho = os.path.join(home, "Downloads")

    def tipo(self, tipo, link):
        self.tipo = tipo
        if self.tipo == 'v':
                self.link = YouTube(link)
        else:
                self.link = Playlist(link)

    def nome(self):
            return f'{self.link.title}'

    def down(self):
        if self.tipo == 'v':
            self.down = self.link.streams.get_highest_resolution()
            print(f'Baixando "{self.nome()}".')
            tela.down(self.down.download(self.caminho))
        else:
            for i in self.link:
                video = YouTube(i)
                stream = video.streams.get_highest_resolution()
                print(f'Baixando "{self.nome()}".')
                tela.down(stream.download(self.caminho))
