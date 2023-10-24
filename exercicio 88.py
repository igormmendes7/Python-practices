from random import randint
from time import sleep
print('♦'*26)
print('      JOGA NA MEGA SENA')
print('♦'*26)
n = int(input("Quantos jogos você quer que eu sorteie? "))
l = []
jogos = []
tot = 0
while tot <= n:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in l:
            l.append(num)
            cont += 1
        if cont >= 6:
            break
    l.sort()
    jogos.append(l[:])
    l.clear()
    tot += 1
print('♦♦♦♦♦♦♦♦SORTEANDO♦♦♦♦♦♦♦♦')
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {l}')
print('☻☻☻☻☻ Boa Sorte ☻☻☻☻☻')