matriz = [[0,0,0],[0,0,0],[0,0,0]]
a = b = d = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para [{l},{c}] : "))
        if matriz[l][c]%2==0:
            d += matriz[l][c]
print('-='*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^4}]',end='')
    print()
print('-='*20)
print(f'A soma dos valores pares é {d}')
for c in range(0,3):
    a += matriz[c][2]
print(f'A soma da terceira coluna é {a}')
for c in range(0,3):
    b +=matriz[1][c]
print(f'A soma da segunda linha é {b}')
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f"O maior valor da segunda linha é {maior}")
