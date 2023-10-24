from random import randint
from time import sleep
from operator import itemgetter #pega o item do dicionario

jogo ={'jogador 1':randint(1,6), #criação do dicionario
       'jogador 2':randint(1,6),
       'jogador 3':randint(1,6),
       'jogador 4':randint(1,6)}

ranking = [] #lista do ranking
print("Valores Sorteados:")

for k, v in jogo.items(): #pega as keys e os values dos items do dicionario
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #ordena os itens pelo valor 1 do dicionario

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos no dado.')
    sleep(1)