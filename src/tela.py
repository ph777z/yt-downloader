from tqdm import tqdm
import os

class tela:
    def __init__(self):
        self.nome = 'YTDownloader'

    def clearScreen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def telaini(self):
        print(r"""
        \\\   ///  |||||||||  ||||\\\     ///|\\\   |||   //\\   |||  ||\\\   |||
         \\\ ///      |||     |||  \\\   ///   \\\  |||  ///\\\  |||  |||\\\  |||
          \\|//       |||     |||   ||| |||     ||| ||| ///  \\\ |||  ||| \\\ |||
           |||        |||     |||  ///   \\\   ///  |||///    \\\|||  |||  \\\|||
           |||        |||     ||||///     \\\|///   ||///      \\\||  |||   \\\||
        
        Enter para iniciar
        """)
        input()
        self.clearScreen()
        
    def menu(self):
        self.clearScreen()
        self.telaini()
        print("""
        Digite:

        p - Para baixar uma playlist
        v - Para baixar um video 
        """)

    def playlist(self):
        self.clearScreen()
        link = input("Link o link da Playlist: ")
        return link

    def video(self):
        self.clearScreen()
        link = input("Digite o Link do Video: ")
        return link

    def downConfirm(self, title):
        baixar = input(f'Baixar "{title}"?(S/N) ').upper()
        if baixar == 'S':
            return True
        else:
            return False

    def down(self, down):
        for i in tqdm(down):
            pass
        
