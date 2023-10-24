#027: Faça um programa que leia o nome completo de uma
# pessoa, mostrando em seguida o primeiro e o último
# nome separadamente.

n = str(input("Digite o nome: " )).strip()
esp = n.count(" ",0,len(n))
n = n.split()
print(f"Seu primeiro nome é:  {n[1]}")
print(f"Seu ultimo nome é:  {n[esp]}")

#Da para usar o Len para contar o numero de palavras dentro de uma lista