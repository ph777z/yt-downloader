import os

class bcolor:
    red = '\033[91m'
    reset = '\033[0m'

class tela:
    def __init__(self):
        self.nome = 'YTDownloader'

    def clearScreen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def telaini(self):
        self.clearScreen()
        print(bcolor.red + r"""
        \\  // ||||||   ||\\     //\\   ||   /\   || |\\   ||
         \\//    ||     || \\   //  \\  ||  //\\  || ||\\  ||
          \/     ||     ||  || ||    || || //  \\ || || \\ ||
          ||     ||     || //   \\  //  ||//    \\|| ||  \\||
          ||     ||     ||//     \\//   |//      \\| ||   \\|
        """ + bcolor.reset + """
        Enter para iniciar
        """)
        input()
        self.menu()
        
    def menu(self):
        self.clearScreen()
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
                    
telaa = tela()