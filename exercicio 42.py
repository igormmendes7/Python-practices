print("==="*9,"\n  Analisador de Triângulos\n","==="*9)

n1 = float(input("Digite o primeiro lado: "))
n2 = float(input("Digite o segundo lado: "))
n3 = float(input("Digite o terceiro terceiro: "))

if n1 < n2+n3 and n2 < n1+n3 and n3 <n1+n2:
    if n1==n2 and n1==n3:
        print("Da pra forma um triangulo Equilatero")
    elif n1==n2 or n2==n3 or n1==n3:
        print("Da pra forma um Triangulo Isósceles")
    else:
        print("Da pra forma um Triangulo Escaleno")
else:
    print("Não da para formar um triangulo ai")

