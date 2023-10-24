'''Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com sua idade: - Se ela ainda vai se alistar ao serviço militar
-se é a hora de se alistar - se já passou do tempo de se alsitar'''
import datetime

hoje = datetime.date.today()

nascimento = input("Digite seu nascimento? ")

nascimento = datetime.datetime.strptime(nascimento, "%d/%m/%Y").date()

hoje1 = hoje.year
nascimento = nascimento.year

if hoje1 - nascimento > 18:
    print(f"Ja passou da hora de se alistar você tem {hoje1-nascimento} Anos")
elif hoje1 - nascimento <18:
    print(f"Falta(m) {18-(hoje1-nascimento)} ano(s) para você se alistar")
else:
    print("Ta na hora de alistar seu safado")

    


