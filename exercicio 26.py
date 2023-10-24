#026: Faça um programa que leia uma frase pelo teclado
# e mostre quantas vezes aparece a letra "A", em que
# posição ela aparece a primeira vez e em que posição
# ela aparece a última vez.

f = str(input("Digite uma frase: ")).lower()
print("O numero de 'A's é: ", f.count("a",0,len(f)))
print("O primeiro 'A' está em: ",f.find("a",0,len(f)))
print("O Ultimo 'A' está em: ",f.rfind("a",0,len(f)))