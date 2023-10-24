''' faça um programa que jogue par ou impar com o computador.
O jogos será interrompido quando o jogador perder mostrando o total de vitorias
consecutivas que ele conquistou no final do jogo'''
from random import randint
jg = cont = 0
pc = randint(1,11)
while True:
    jg = str(input("Par ou Impar? ").lower().strip())
    if jg == 'impar':
        n = int(input("Escolha um número impar: "))
    else:
        n = int(input("Escolha um número par: "))
    resultado = n+pc
    print(f"Você jogou {n} e o computador jogou {pc} e o resultado foi {resultado}")
    if resultado %2 == 0 and jg == 'par':
        cont +=1
    elif resultado %2 == 1 and jg == 'impar':
        cont +=1
    else:
        break
print(f"Dessa vez você perdeu mas Você ganhou {cont} vez(es)")