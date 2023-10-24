'''Desenvolva um programa que leia 4 valores no teclado e guarde na tupla
a - qnts x vc digitou o numero 9
b - em que posição foi digitado o primeiro valor 3
c - quantis foram os nmeros pares'''
cont = 0
tupla = int(input("Digite um numero: ")),int(input("Digite um numero: ")),int(input("Digite um numero: ")),int(input("Digite um numero: "))
print(f"O numero 9 apareceu {tupla.count(9)} vez(es)")

if tupla.count(3) > 0:
    print(f"O número 3 está na posição {tupla.index(3)}")
else:
    print("O número 3 não foi digitado")
print(f"Foram digitados os valores: ",end="")
for par in tupla:
    if par%2==0:
        print(par, end=' ')


