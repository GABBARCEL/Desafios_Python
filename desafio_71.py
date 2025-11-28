# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado 
# (número inteiro) e o programa vai  informar quantas cédulas de cada valor serão entregues. 
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("=================================\nBANCO CEV\n=================================")
valor = int(input("Valor do saque: R$"))
ced50 = 0
ced20 = 0
ced10 = 0
ced1 = 0

total = valor

while True:
    if total >= 50:
        total -= 50
        ced50 += 1
    else:
        if total >= 20:
            ced20 += 1
            total -= 20
        elif total >= 10:
            ced10 += 1
            total -= 10
        elif total >= 1:
            ced1 += 1
            total -= 1
        else:
            break

print(f"você tem agora: \n{ced50} cédulas de R$50\n{ced20} cédulas de R$20\n{ced10} cédulas de R$10\n{ced1} cédulas de R$1")
    