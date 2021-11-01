# YTDOWN <a name=adsd></a>

Baixar videos do youtube com python.

- [Como Instalar?](#como-instalar)
- [Como Usar?](#como-usar?)
- [navegação](#navegação)
- [Considerações](#considerações)
- [Dependências](#dependências)


## Como Instalar?

Primeiro é preciso instalar o python, para baixar [clique aqui](https://www.python.org/).

Após instalar, clone este repositório e abra o terminal na pasta clonada, feito isso, execute o comando `pip install -r requirements.txt`. 

Pronto, agora você já pode baixar os seus vídeos!

## Como Usar?

Para abrir, use um gerenciador de arquivos e com o python abra o arquivo `main.py`, ou com o terminal aberto na pasta raiz do programa, execute o comando`python(ou python3) main.py`.

Com o programa aberto, será exibida a tela a seguir:

![Tela inicial](/docs/tela-inicial.png)

Basta clicar a tecla `Enter` e será exibido o menu a seguir:

![Menu](/docs/tela-menu.png)

Escolhendo uma das opções, clique `Enter` novamente.

Após isso, deverá ser informado o link da playlist ou video e digite `Enter`, será informado o titulo e perguntado se realmente deseja baixar, se sim, digite `s` e clique `Enter`. Caso tenha dificuldade com a opção colar ou não saiba como voltar ao menu, leia a parte de [navegação](#navegação)

![Download Video](/docs/down-video.jpg)
![Download Playlist](/docs/down-playlist.jpg)

Pronto, você acabou de aprender a usar o YTDOWN!

## Navegação

Colar: `Ctrl + Shift + V`
Voltar: `Ctrl + C`

## Considerações
- No momento não é possível selecionar a resolução desejada, apenas baixar na resolução mais alta disponivel no video.
- Este programa só foi testado no sistema linux, por este motivo é possível que se tenha problemas ao usar em outro SO.

## Dependências

[Pytube 11.0.1](https://pytube.io/en/latest/)

