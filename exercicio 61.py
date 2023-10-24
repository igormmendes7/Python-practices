'''ler o primeiro termo e a razão de uma PA e mostre
os 10 primeiros termos da progressão com while'''

pt = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
c = 1
termo = pt
while c <= 10:
    print(f"{termo} -> ", end='')
    termo += r
    c += 1
print('FIM')
