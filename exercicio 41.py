'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria de acordo com a idade'''

a = str(input("Digite o seu nome: "))
ia = int(input(f"Qual a sua idade {a}? "))

 
if ia <= 9:
    print(f"Você está na categoria Mirin {a.title()}")
elif ia > 9 and ia <= 14:
    print(f"Você está na categoria Infantil {a.title()}")
elif ia > 14 and ia <= 19:
    print(f"Você está na categoria Junior {a.title()}")
elif ia > 19 and ia <=20:
    print(f"Você está na categoria Sênior {a.title()}")
else:
    print(f"Você está na categoria master")



    


