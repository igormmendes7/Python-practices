'''Crie um programa que vai gerar cinco numeros aleatórios e colocar em
 uma tupla. Depois disso mostre a listagem de numeros gerados e também indique
 o menor e o maior valor que estão na tupla'''

from random import randint
sorteio = randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)
print(f"foram sorteados os números {sorteio[0]} {sorteio[1]} {sorteio[2]} {sorteio[3]} {sorteio[4]}")
ordem = sorted(sorteio)
print(f"O menor volume é {ordem[0]}\nO menor valor é {ordem[4]}")