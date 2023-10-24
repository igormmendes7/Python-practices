'''Desenvolva um programa que leio o NOME, IDADE e sexo de 4 pessoas. No final do programa
mostre:  A media de idade do grupo, qual o nome do homem mais velho e quantas mulheres tem menos de 20 anos'''
import datetime

hoje = datetime.date.today()
somaidade = 0
maioridadehomem = 0
nomevelho = ''
mulheres = 0

for i in range(1,5):
    print(f'-----{i}ª PESSOA -----')
    nome = str(input("NOME: ").strip().title())
    nascimento = input("DATA DE NASCIMENTO(dd/mm/aaa)? ")
    nascimento = datetime.datetime.strptime(nascimento, "%d/%m/%Y").date()
    sexo = str(input("SEXO [M/F]: ").upper())
    if hoje.month < nascimento.month: #Condiação para calcular a idade com base no mês atual
        idade = hoje.year-nascimento.year-1
    else:
        idade = hoje.year-nascimento.year
    somaidade += idade
    if i == 1 and sexo == 'M': #Caso tenha apenas 1 pessoa digita com sexo M, ele vai ser a maior idade
        maiorirdadehomem = idade #como esse é a maior idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem: #caso a nova idade seja maior doque a idade anterior, essa será a nova idade
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20: #caso tenha uma mulher com menos de vinte anos, essa sera contada na linha abaixo
        mulheres += 1
mediaidade = somaidade/4
print(f"A média de idade do grupo é de {mediaidade:.2f} anos")
print(f"O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}")
print(f"Ao todo são {mulheres} mulheres menores de 20 anos")