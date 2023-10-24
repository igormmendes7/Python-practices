'''Crie um programa que leia duas notas de um aluno e calcule sua media
mostrando uma mensagem no final de acordo com a média atingida'''

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1+n2+n3)/3

if media <5.0:
    print(f"Média {media:.1f}, você foi REPROVADO")
elif media>=5.0 and media < 6.9:
    print(f"Média {media:.1f}, RECUPERAÇÃO")
else:
    print(f"Média {media:.1f}, você foi APROVADO")


    


