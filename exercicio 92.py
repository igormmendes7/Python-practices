from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['genero'] = str(input("Digite o seu gênero (H)-Homem (M)-Mulher: ")).upper().strip()
dados['CTPS'] = int(input("Carteira de trabalho (digite 0 caso não tenha): "))
if dados['CTPS'] != 0:
    dados['Contratado'] = int(input("Digite o ano de contratação: "))
    dados['Salario'] = float(input("Digite o seu salário: R$" ))
    if dados['genero'] == 'M':
        dados['Aposentadoria'] = (dados['Contratado']+35)-nasc
    else:
        dados['Aposentadoria'] = (dados['Contratado']+32)-nasc

print(dados)
for k, v in dados.items():
    print(f'{k:<15} •••► {v:<6}')