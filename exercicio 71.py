'''caixa eletronico'''
print("="*30)
print("{:^30}".format("BANCO TESTE"))
print("="*30)
valor = int(input("Digite um valor para saque: R$"))
total = valor #o total é o valor digitado
cedula = 100 #começo com a cedula maior
totalcedula = 0 #contador de cedula
while True: #loop infinito
    if total >= cedula: #se o total for maior que a cédula
        total -= cedula #diminui o valor da cedula do total
        totalcedula += 1 #conta mais 1 no numero de cedulas
    else: #caso o total seja menor que o valor da cedula
        if totalcedula>0: #se o total de cedulas for maior que um então ele imprime
            print(f"Total de {totalcedula} cédulas de R${cedula}")
        if cedula == 100:
            cedula  = 50
        elif cedula == 50: #se a cedula atingir 50 eu n consigo mais tirar 50
            cedula = 20 #então a cedula passa a ser 20
        elif cedula == 20: #se a cedula atingir 20...
            cedula = 10#passa a ser 10
        elif cedula == 10:#se a cedula atingir 10...
            cedula = 5 #passa a ser 5....
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        totalcedula = 0 #cada vez q muda a nota o total de cedula zera
        if total == 0: #se for zero para
            break
print("="*20)
print("{:^30}".format("VOLTE SEMPRE"))