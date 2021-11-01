from pytube import YouTube, Playlist

class down:
    def __init__(self, tipo, link):
        self.tipo = tipo
        if self.tipo == 'video':
            self.link = YouTube(link)
            self.down = self.link.streams.get_highest_resolution()
        else:
            self.link = Playlist(link)


    def nome(self):
        self.nome = self.link.title
        return (f'{self.nome}')

    def down(self):
        if self.tipo == 'video':
            self.down.download()
        else:
            for i in self.link:
                video = YouTube(i)
                stream = video.streams.get_highest_resolution()
                stream.download()
