from random import randint

c = randint(0,5)

print("=*="*17,"\n Vou pensar em um numero, consegue adivinhar qual? \n","=*=" *17)

n = int(input("Digite um numero de 0 a 5: "))

if n == c :
    print("Você certou!!")
else:
    print(f"Você errou!! na verdade eu tinha pensando em {c}")

