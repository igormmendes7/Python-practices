l = [[] , []]
valor = 0
for c in range (1,8):
    n = int(input(f"Digite o {c} valor: "))
    if n%2==0:
        l[0].append(n)
    elif n%2==1:
        l[1].append(n)
    l.sort()
print(l[0])
print(l[1])
