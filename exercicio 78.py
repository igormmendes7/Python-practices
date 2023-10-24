'''faça um programa que leia 5 valores numericos e guarde os em lista
no final, mostre qual foi o maior e o menor valor digitado e as suas
respectivas posições na lista'''
list = []
for c in range(0,5):
    list.append(int(input("Digite um numero: ")))
a = max(list)
b = min(list)
print(f"O maior valor é {a} na posição {list.index(a)+1}")
print(f"O menor valor é {b} na posição {list.index(b)+1}")
