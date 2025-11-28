# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    quest = int(input("Digite um número: "))
    lista.append(quest)

    quest2 = input("Quer continuar? [S/N]: ")

    if quest2.upper() == "N":
        break


print(f"você digitou {len(lista)} valores\nA lista ordenada de fomra crescente fica {sorted(lista)}\nE de forma decrescente {sorted(lista, reverse=True)}")