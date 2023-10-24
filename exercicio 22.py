# 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas
#Quantas letras aotodo sem considerar espaços Quantas letras tem o primeiro nome
nome = input("Digite o seu nome: ")
qnt = nome.count(" ")
contar = len(nome) - qnt
pn = nome.split()
print(f"{nome.upper()}\n{nome.lower()}\n{contar} Caracteres")
print(len(nome), len(pn[1]))
