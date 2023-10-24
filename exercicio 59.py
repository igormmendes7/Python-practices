'''Crie um programa que leia dois valores
e mostre um menu na tela:
[1]soma
[2]multiplicar
[3]Maior
[4]Novos numeros
[5]Sair do programa '''

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
p = 0 
while p != 5: #enquanto p não for igual a 5 ele vai da as opções
    p = int(input('''Digite:
    [1] para somar
    [2] para Multiplicar
    [3] para mostrar o maior numero
    [4] para novos numeros
    [5] Para sair
    >>>>>>>>>>Escolha: '''))
    if p == 1: #se opção 1 execute abaixo
        soma = n1+n2
        print(f"A soma entre {n1} e {n2} é {soma}")
    elif p == 2: 
        mult = n1*n2
        print(f"A multiplicação entre {n1} e {n2} é {mult}")
    elif p == 3:
        if n1 > n2:
            print(f"O maior é {n1}")
        else:
            print(f"O maior é {n2}")
    elif p == 4:
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
    elif p ==5: #sairá do loop
        print("Adeus!")
    else: #caso a opção seja invalida
        print("Opção invalida")