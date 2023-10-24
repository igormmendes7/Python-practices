'''Elabore um progrma que calcule o valor a ser pago por um produto
considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO
-À VISTA DINHEIRO E CHEQUE = 10% DE DESCONTO
-À VISTA NO CARTÃO = 5% DESCONTO
-EM ATÉ 2X NO CARTÃO =  PREÇO NORMAL
-3X OU MAIS NO CARTÃO 5% DE JUROS AO MÊS'''

valor = float(input("Digite o valor do produto: R$"))
pag = int(input("Qual a forma de pagamento? \n 1 - À VISTA NO DINHEIRO OU CHEQUE\n 2 - À VISTA NO CARTÃO\n 3 - DIVIDO NO CARTÃO \n :"))
if pag == 1:
    valor = valor*0.9
    print(f"O produto sairá por R${valor:.2f}")
elif pag == 2:
    valor = valor*0.95
    print(f"O produto sairá por R${valor:.2f}")
else:
    p = int(input("Digite a quantidade de parcelas: "))
    if p == 2:
        print(f"O produto sairá por R${valor:.2f}")
    else:
        valor = (valor*0.05*p)+valor
        print(f"O produto sairá por R${valor:.2f} com {p} parcelas de {valor/p:.2f}")
        