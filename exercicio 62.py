'''ler o primeiro termo e a razão de uma PA e mostre
os 10 primeiros termos da progressão com while'''

pt = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
c = 1
termo = pt
n = 0
mais = int(input("Digite quantos termos quer que apareça: ")) #defini como 10 termos iniciais
while mais != 0: #enquanto o termo for diferente de 0
    n += mais #ele vai somar N com o numero de termo
    while c <= n: #condição da PA 
        print(f"{termo} -> ", end='')
        termo += r #o termo soma com a razão
        c += 1 #conta qnts deu
    print('Pausa') #dps q termina essa condição entra na outra
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f"Progressão finalizada com {n} termos mostrados")