'''Escreva um programa para aprovar o empréstimo bancario para a compra
de uma casa. O programa vai perguntar o VALOR DA CASA, o SALARIO do comprador e 
em QUANTOS ANOS ele vai pagar. CALCULE O VALOR DA PRESTAÇÃO MENSAL SABENDO QUE
ELA NÃO PODE EXCEDER 30% DO SALARIO OU ENTÃO O EMPRESTIMO SERÁ NEGADO'''

print("=+="*11 , "\n Vamos simular seu emprestimo!!\n" , "=+="*11)

casa = float(input("Digite o valor da casa: R$"))
salario = float(input("Por favor, informe sua renda mensal: R$"))
pag = int(input("Em quanto tempo pretende pagar a casa(em anos)? "))

prestação = casa/(pag*12)
if  prestação < (salario*0.3):
    print(f"O seu emprestimo de R${casa:.2f} foi aprovado com {pag*12} parcelas de R${prestação}!!")
else:
    print(f"O seu emprestimo de R${casa:.2f} foi negado!!")
    


