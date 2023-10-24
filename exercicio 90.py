aluno = dict()

aluno['Nome'] = str(input('Nome do Aluno: '))
aluno['Media'] = float(input('Qual a media do aluno? : '))
if aluno['Media'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'

print(f'O Aluno {aluno["Nome"]} está {aluno["situação"]} com média {aluno["Media"]}')
