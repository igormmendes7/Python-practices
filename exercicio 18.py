import math
a = float(input("Digite o angulo: "))


s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print(f'O angulo {a}º possui o cosseno {c}, o seno {s} e a tangente {t}')
