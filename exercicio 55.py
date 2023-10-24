'''Faça um programa que leia o peso de 5 pessoas e no final mostre qual foi o maior e o menor'''
maior = 0 
menor = 0
for i in range(1,6):
    p = float(input(f"Digite o peso da {i}ª Pessoa: "))
    if i == 1:
        maior = i
        menor = i
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f"O Maior peso lido foi de {maior:.2f} e o menor peso foi {menor:.2f}kg")