'''escreva um programa que leia um número N inteiro e mostre na tela
os n primeiros elementos de uma sequência de fibonacci'''

n = int(input("Digite um numero inteiro?"""))
fb = 0
f = 1
count = 0
while count != n:
    fibo = fb + f
    f = fb
    fb = fibo
    count += 1
    print(fibo, end=" -> ")
print("Fim")
