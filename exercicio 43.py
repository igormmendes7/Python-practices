'''logica que leia o peso e a altura e calcule IMC
e mostra seu status de acordo com: - abaixo de 18.5 = abaixo do peso
entre 18.5 e 25: Peso ideal, 25 até 30: sobrepeso, 30 a 40: Wigor, acima de 40: Luiz'''

print("=*="*5, "\nCalculo IMC\n","=*="*5)

peso = float(input("Digite seu peso: "))
altura = float(input("Digite a sua altura: "))

IMC = peso/(altura**2)

if IMC < 18.5:
    print(f"IMC {IMC:.2f} =  Abaixo do peso")
elif IMC >= 18.5 and IMC < 25:
    print(f"IMC {IMC:.2f} = Peso ideal")
elif IMC >= 25 and IMC < 30:
    print(f"IMC {IMC:.2f} = sobrepeso")
elif IMC >= 30 and IMC <40:
    print(f"IMC {IMC:.2f} = Wigor")
else:
    print(f"IMC {IMC:.2f} = Luiz")
