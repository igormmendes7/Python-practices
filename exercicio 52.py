'''faça um programa que leia um número inteiro
e diga se ele é ou não um número primo'''

n = int(input("Digite um número: "))
cont = 0

for c in range(1,n+1):
    if n % c == 0:
        cont += 1
        print(f"{n} é divisivel por {c} que é igual à {n/c}" , end= "\n")
print(f"O numero {n} foi divido {cont} vezes")
if cont == 2:
    print("\033[32mO número é primo")
else:
    print("\033[31Ou seja, não é não é primo")