alunos = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1:'))
    nota2 = float(input('Nota2: '))
    media = (nota1+nota2)/2
    alunos.append([nome,[nota1,nota2],media]) #nota 1 e 2 estão na mesma matriz (segunda)
    resp = str(input("Quer continuar [S/N]?"))
    if resp in 'Nn':
        break
print('▬'*15)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('▬'*15)
for i, a in enumerate(alunos): #i é o numero, a é a referencia na matriz
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}') #a 0 é o nome a 2 é a media
while True:
    print('▬'*15)
    opc = int(input("Mostrar notas de qual aluno? (-1 para finalizar): "))
    opc -= 1
    if opc == -2 :
        break
    if opc <= len(alunos) - 1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
print('▬▬▬▬▬▬Até breve▬▬▬▬▬')