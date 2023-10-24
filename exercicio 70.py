'''crie um progrma que leia nome e preço de varios proodutos
O programa deverá perguntar se o usuario deseja ou não coontinuar e deve mostrar:
A- QUAL O TOTAL GASTO
B - QUANTOS PRODUTOS CUSTAM MAIS DE RS1000
C - QUAL É O NOME DO PRODUTO MAIS BARATO'''
nomemenor = ' '
cont = menor = total = contmil = 0
while True:
    nome = str(input("Digite o nome do produto: ").strip().lower())
    valor = float(input("Digite o valor do produto: R$"))
    total += valor # soma dos valores
    cont += 1
    if cont == 1:
        menor = valor
        nomemenor = nome
    elif valor < menor:
        menor = valor
        nomemenor = nome #associa o nome do produto que tem menor valor
    if valor > 1000: #QNTS CUSTAM MAIS DE 1000
        contmil += 1
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input("Deseja Continuar[S/N]? ")).upper().strip()
    if continuar == 'N':
        break
print(f"O total gasto foi R${total:.2f}")
print(f"Há {contmil} produto(s) que custa(m) mais de R$1000,00")
print(f"O produto mais barato é o {nomemenor.title()} e ele custa {menor:.2f}")
