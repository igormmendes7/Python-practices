'''Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até 20'''
'''seu programa deverá ler um número pelo teclado entre 0 e 20 e mostra-lo
por extenso'''

contagem = "zero","Um","Dois","Três","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez","Onze","Doze","Treze","Quatorze","Quinte","Dezesseis","Dezessete","Dezoito","Dezenove","Vinte"
a = int(input("Digite um número entre 0 e 20:"))
while a > 20 or a < 0:
    a = int(input("Digite um número entre 0 e 20: "))
print(f"Você digitou o número {contagem[a]}")