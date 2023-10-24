'''Faça um programa que mostre uma contagem
regressiva com qualquer numero até 0 com pausa de 1segundo'''

import time
n = int(input("Digite quanto tempo deseja: "))
for c in range(n,0,-1):
    time.sleep(1)
    print (c)
time.sleep(1)
print("BOOOM")