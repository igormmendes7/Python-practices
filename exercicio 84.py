pessoas = list() #lista de pessoas
aux = list() #lista auxiliar
maior = menor = 0 #define as variaveis mairo e mnor
c = 's'
while c[0] != 'n':
    aux.append(str(input("Nome: "))) #input direto na lista auxiliar
    aux.append(str(input("Peso: ")))
    if len(pessoas) == 0: #se o numero de pessoas for 0
        maior = menor = aux[1] #então o maior e menor é o aux 1
    else:
        if aux[1] > maior:
            maior = aux[1]
        if aux[1] < menor:
            menor = aux[1]
    pessoas.append(aux[:]) #adiciona uma copia da lista auxiliar na lista pprincipal
    aux.clear() #limpa a lista auxiliar
    c = str(input("Quer continuar [S/N]? ")).strip().lower()

print('=='*30)
print(f'Você cadastrou {len(pessoas)} pessoas')
print('=='*30)
print(f'O maior peso foi de {maior}Kg. Peso de ',end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi de {menor}Kg. Peso de ',end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}')
