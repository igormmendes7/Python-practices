''' Crie um programa que leia vaior números inteiros, no final da execução
mostre a média entre todos os valores e qual foi o maior e o menor valor lido
O programa deve perguntar o usuario se ele quer continuar ou não'''

maior = menor = cont = n = c = 0
continuar = 'S'
while continuar == 'S':
    n = int(input("Digite um número: "))
    cont += 1
    c += n
    continuar = str(input("Deseja continuar? [S/N]").strip().upper())
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior =  n
        if n < menor:
            menor = n
media = c/cont

print(f"Foram digitados {cont} número e a média deles é é : {media}")
print(f"O maior numero foi {maior} e o menor número foi {menor}")

