'''crie uma tupla preenchida com os 20 primeiros colocados da tabela
do campeonato brasileiro de futebol. Na ordem de colocação depois mostre:
A - Apenas os 5 primeiros colocados
B -  os ultimos 4 colocados da tabela
C - uma lista com os times em ordem alfabetica
D - em que posição na tabela está o tipo de chapeco'''

tabela = "Palmeiras","Flamengo","Internacional","Grêmio","São Paulo","Atlético-MG","Athletico-PR","Cruzeiro","Botafogo","Santos","Bahia","Fluminense","Corinthians","Chapecoense","Ceará","Vasco","Sport","América-MG","Vitória","Paraná"
print(f"Os 5 primeiros colocados são {tabela[0:5]}")
print(f"Os 4 ultimos colocados são {tabela[16:20]}")
print(sorted(tabela))
print(f"A Chapecoense está na {tabela.index('Chapecoense')+1}ª posição")