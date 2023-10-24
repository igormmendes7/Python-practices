'''construa 10 termos de uma PA'''

print("="*20, "\n 10 TERMOS DE UMA PA\n", "="*20 )


n = int(input("Primeiro termo: "))
r = int(input("Digite a razão: "))

if r == 0:
    print("Não é possivel realizar o calculo. Tente novamente")
else:
    for c in range(n,((n+(10-1))*r)+r,r):
        print(c,end=" -> ")
    print("Acabou")