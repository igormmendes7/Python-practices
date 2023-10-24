'''Crie um programa que leia uma frase qualquer
e diga se ela é um palíndromo, desconsiderando os espaços'''

a = str(input("Digite uma frase: ").lower().strip())
p = a.split()
junto = ''.join(p)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if junto == inverso:
    print("palíndromo!")
else:
    print("Não é palindromo!")