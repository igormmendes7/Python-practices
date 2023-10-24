v = float(input("Digite a velocidade do carro: "))

if v > 80:
    multa = (v-80)*7
    print(f"Toma multa de R${multa:.2f} trouxa!")
else:
    print("continua ai!")