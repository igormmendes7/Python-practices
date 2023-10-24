'''crie um programa que tenha uma tupla unica com nomes de
produtos e seus respectivos preços, na sequencia
mostre uma listagem de preços organizando os dados de forma tabular'''

compras = "Lapís",1.75,"Borracha",2.00,"Caderno",15.90,"Estojo",25.00,"Transferidor",4.20,"Compasso",9.99,"Mochila",120.32,"Canetas",22.30,"Livro",34.90
print("_"*30)
print("     LISTAGEM DE COMPRAS     ")
print("-"*30)
for c in range (0,len(compras),2):
    print(f"{compras[c]:-<20} R$: {compras[c+1]:>6.2f}") #formatando
                       #numero de posições no alinhamento
