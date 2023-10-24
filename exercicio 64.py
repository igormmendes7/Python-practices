'''Crie um programa que leiva vários numeros inteiros, O programa só vai parar
quando o usuario digitar 999 que é a condição de parada, no final
mostre quantos núermos foram digitados e qual foi a soma entre eles'''

n = c = 0
cont = 0
while n != 999:
    n = int(input("Digite um numero:"))
    c += n #não possolocar n pq altera o valor de N para flag
    cont += 1
print(f"A soma de tudo é {c-999} e foram digitadoos {cont-1} números")



