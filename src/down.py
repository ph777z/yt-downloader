from pytube import YouTube, Playlist
from pytube.cli import on_progress
from src.tela import telaa as tela
import time
import os


home = os.path.expanduser('~')

class down:
    def __init__(self):
        self.caminho = os.path.join(home, "Downloads")

    def tipo(self, tipo, link):
        self.tipo = tipo
        if self.tipo == 'v':
                self.link = YouTube(link, on_progress_callback=on_progress)
        else:
                self.link = Playlist(link)

    def nome(self):
            return f'{self.link.title}'
    
    def filesize(self, sizebytes):
        mbsize = round(sizebytes*(9.537*10**(-7)), 2)
        return mbsize

    def down(self):
        if self.tipo == 'v':
            self.down = self.link.streams.get_highest_resolution()
            print(f'Baixando "{self.nome()}" - {self.filesize(self.down.filesize_approx)}MB')
            self.down.download(self.caminho)
            print()
            print(f'"{self.nome()}" Baixado.')
            time.sleep(5)
        else:
            for i in self.link:
                video = YouTube(i, on_progress_callback=on_progress)
                stream = video.streams.get_highest_resolution()
                print(f'Baixando "{video.title}" - {self.filesize(stream.filesize_approx)}MB')
                stream.download(self.caminho)
                print()
            print(f'"{self.nome()} Baixado. ')
            time.sleep(5)
