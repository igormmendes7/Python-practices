'''Desenvolva um programa que leia SEIS NUMEROS INTEIROS
e mostre a soma apenas daqueles que forem pares, se o valor
digitado for ímpar. Desconsidereo'''
soma = 0
cont = 0
for i in range(1,7):                        
    n = int(input(f"Digite o {i} número: "))
    if n%2==0:
        soma += n
        cont += 1
print(f"Você informou {cont} números Pares e a soma foi {soma}")