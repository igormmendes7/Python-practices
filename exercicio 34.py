'''Escreva um programa que pergunte o salário de um funcinário
e calcule o valor do seu eumento, para salarios maiores que 
1250 o aumento de 10% para menor ou iguais o aumento é de 15%'''

s = float(input("Digite o valor do seu salario atual: "))

if s > 1250:
    s1 = s*1.10
else:
    s1 = s*1.15

print(f"Quem ganhava R${s:.2f} agora ganha R${s1:.2f}")
