'''Escreva um programa que LEIA DOIS NUMEROS INTEIROS e compare-os,
mostrando na tela uma mensagem: O primeiro valor é maior, o segundo valor é maior
e Não existe valor amior, os dois são iguais'''

print("=/=+=*=-="*3, "\n Vamos comparar os numeros??\n","=/=+=*=-="*3)

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

if n1 > n2:
    print(f"O primeiro valor '{n1}', é o maior")
elif n2 > n1:
    print(f"O segundo valor '{n2}', é o maior")
else:   
    print("Nenhum valor é maior, uma vez que ambos são iguais")



    


