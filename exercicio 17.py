import math
c = float(input("Digite o cateto oposto: "))
c2 = float(input("Digite o cateto adjacente: " ))

h = math.hypot(c,c2)

print(f'A hipotenusa do Triangulo é {h}')
