'''Faça um programa que leia o ano de nascimento de 7 pessoas e informe se já são de maior'''
import datetime

hoje = datetime.date.today()

for i in range(1,8):
    nascimento = input("Digite seu nascimento? ")
    nascimento = datetime.datetime.strptime(nascimento, "%d/%m/%Y").date()
    if hoje.month < nascimento.month:
        hoje1 = hoje.year
        nascimento = nascimento.year
        i = nascimento
        if hoje1-(i-1)>18:
            print(f"{hoje1-i-1} Anos, entrada permitida!")
        else:
            print("BARRADO, você é de menor")
    else:
        hoje1 = hoje.year
        nascimento = nascimento.year
        i = nascimento
        if hoje1-i>18:
            print(f"{hoje1-i} Anos, entrada permitida!")
        else:
            print("BARRADO, você é de menor")