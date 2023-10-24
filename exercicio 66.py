'''Crie um programa que leia varios numeros inteiros pelo teclado, só pare quando digitar
999 e mostre qnts numeros foi digitado e a soma entre eles'''

n = cont = soma = 0
while True:
    n = int(input("Digite um número (999 para parar): "))
    if n == 999:
        break
    cont += 1
    soma += n
print(f"Foram digitados {cont} números e a soma entre eles é {soma}")