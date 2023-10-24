#faça um programa que leia três numeros e mostre qual é o maior
#e qual é o menor

n1,n2,n3 = int(input("Digite o primeiro numero: ")),int(input("Digite o segundo numero: ")),int(input("Digite o terceiro numero: "))

if n1 < n2 and n1 < n3:
    print(f"O menor numero é Primeiro: {n1}")
elif n2 < n1 and n2 < n3:
    print(f"O menor numero é Segundo: {n2}")
else:
    print(f"O menor numero é Terceiro: {n3}")
