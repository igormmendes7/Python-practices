'''palavras na tupla e verificar quais são as vogais'''

tupla = input(),input(),input(),input(),input(),input()

for p in tupla:
    print(f"\nNa palavra {p} temos as vogais: ",end="") #vai printar o for sempre
    for letra in p: #
        if letra.lower() in 'aeiou': #verifica se tem alguma das vogais na p
            print(letra, end=",")


