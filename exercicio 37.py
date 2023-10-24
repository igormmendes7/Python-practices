'''Escreva um programa que leia um numero inteiro qualquer e peça para o usuario
escolher qual será a base para conversão, 1 PARA BINARIO, 2 PARA OCTAL E 3 PARA HEXADECIMAL'''

print("=-=-"*10 , "\n Vamos converter um numero??\n", "=-=-"*10)

n = int(input("Digite um numero inteiro: "))
c = int(input("Digite 1 para converter para Binario, 2 para Octal e 3 para Hexadecimal :"))

if c == 1:
    binary = format(n,"b") #formata o numero, b  bin, o octal, x hex, d decimal, E cientif, X hex maiusculo
    print(f"O numero {n} em binario é {binary}")
elif c == 2:
    octal = format(n, "o")
    print(f"O numero {n} em Octal é {octal}")
else:
    hex = format(n,"x")
    print(f"O numero {n} em Hexadecimal é {hex}")



    


