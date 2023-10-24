'''Programa que leia a idade e o sexo de várias pessas
A cada pessoa cadastrada o programa deverá perguntar se o usuario deseja continuar ou não
mostre no final: quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados
e quantas mulheres tem menos de 20 anos'''

tot18 = conthomem = contmulher = 0

while True:
    idade = int(input("Digite a sua idade: "))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input("Digite o seu sexo [M/F]:" ).upper().strip())[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        conthomem += 1
    if sexo == 'F' and idade < 20:
        contmulher += 1
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input("Deseja Continuar[S/N]? ").upper().strip())[0]
    if continuar == 'N':
        break
print(f"Foram cadastradas {tot18} Pessoas com mais de 18 anos")
print(f"No total de {conthomem} homens")
print(f"E {contmulher} mulheres com menos de 20 anos")