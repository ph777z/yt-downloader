from pytube import Playlist, YouTube
from pytube.request import stream
import src.prints as p

def video():
    p.clean_screen()
    print('Digite o link do video:')
    yt = YouTube(input())
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print(f'{yt.title} Baixado.')
    p.down_concluded('video')

def playlist():
    p.clean_screen()
    print('Digite o link da playlist:')
    plist = Playlist(input())
    print(f'{plist.title}')
    for videos in plist.videos:
        print(f'Baixando: {videos.title}')
        stream = videos.streams.get_highest_resolution()
        stream.download()
    print(f'A playlist {plist.title} foi baixada.')
    p.down_concluded('Playlist')
