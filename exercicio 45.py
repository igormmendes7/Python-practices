'''Crie um programa que o computador jogue JOKENPO'''
import random 

c = random.randint(1,3)

if c == 1:
    c = str("pedra")
elif c == 2:
    c = str("papel")
else:
    c = str("tesoura")
    
p = str(input("Escolha Pedra, Papel ou Tesoura: ").lower().strip())


if p == "pedra" and c == p or p == "papel" and c == p or p == "tesoura" and c == p:
    print(f"Com minha/meu {c.upper()} e a sua/seu {p.upper()} deu Empate")
elif p == "pedra" and c == "papel" or p == "papel" and c == "tesoura" or p == "tesoura" and c == "pedra":
    print(f"Com minha/meu {c.upper()} e a sua/seu {p.upper()} Você perdeu")
else:
    print(f"Com minha/meu {c.upper()} e a sua/seu {p.upper()} Você Ganhou")
