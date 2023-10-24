'''faça o computador pensar em um numero
entre 0 e 10. O jogador deve tentar advinhar até
acertar'''
import random

jogador = int(input("Digite um numero: "))
a = random.randint(1,10)
cont = 1
while jogador != a:
    jogador = int(input(f"Eu pensei em {a} e você digitou {jogador}, tente novamente: "))
    a = random.randint(1,10)
    cont += 1
print(f"Agora sim, dps de {cont} tentativas Acertou miseravi!")