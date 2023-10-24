'''Caculadora de fatorial'''
'''import math
n = int(input("Digite um número para calcular seu fatorial: "))
print(f'O fatorial de {n} é :', math.factorial(n))'''

n = int(input("Digite um número: "))
c = n
f = 1
while c > 0:
    print(f"{c}", end="") #
    print(' x ' if c >1 else ' = ', end='') #condição no print
    f *= c #fatorial é o F x o C que recebe n valores
    c -= 1 #como o C diminuiu, ele entra em loop
print(f"{f}")
