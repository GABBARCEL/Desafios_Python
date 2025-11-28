# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores 
# pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []

while True:
    entry = int(input("Digite um número: "))
    lista.append(entry)

    if entry % 2 == 0:
        pares.append(entry)
    else:
        impares.append(entry)

    
    verefy = input("Você quer continuar? [S/N]: ")

    if verefy.upper() == "N":
        break

print(f"os números digitados foram: {lista}\nOs números pares são {pares}\nOs ímpares são {impares}")