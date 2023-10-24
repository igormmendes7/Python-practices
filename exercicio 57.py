''' faça um programa que leia o sexo de uma pessoa
mas só aceite valores M e F. Caso esteja errado
peça a digiação novamente até ter um valor correto'''

s = ''
while s != 'M' and s != 'F':
    s = str(input("Digite o sexo: ").upper().strip())
    if s != 'M' and s != 'F':
        print("Digite apenas 'M' ou 'F'")
print("OK")