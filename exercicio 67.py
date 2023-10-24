'''faça um programa que mostre a tabuada de varios numeros, um de cada vez para cada valor
digitado pelo usuario. O programa é interrompido quando o numero solicitado for negativo'''


while True:
    n = int(input("Tabuada de qual valor? "))
    if n < 0:
        print("Não é possivel realizar com numero negativo!")
        break
    for c in range (1,11):
        print(f"{n} x {c} = {c*n}", end='\n')
print("ADEUS")

