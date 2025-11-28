# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = 0
pdrt_caros = 0
m_barato = [0, 0]

print("---------------------------------------------------\n")
print(" ~ REGISTRO DE PRODUTOS ~\n")
print("---------------------------------------------------")


while True:
    prt = str(input("Nome do produto: ")).strip()
    valor = int(input("Valor do produto: R$"))

    if valor > 1000:
        pdrt_caros += 1
    
    if m_barato[0] == 0:
        m_barato[1] = prt
        m_barato[0] = valor
    else:
        if m_barato[0] > valor:
            m_barato[1] = prt
            m_barato[0] = valor
    
    total += valor
    
    quest = str(input("Você quer continuar? [S/N]: ")).strip().upper()

    if quest == "N":
        break
    
print(f"há R${total} em produtos\n{pdrt_caros} produtos que custam mais de R$1000\nO produto mais barato é o {m_barato[1]}, custando R${m_barato[0]}")