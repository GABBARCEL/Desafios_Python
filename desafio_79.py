# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, 
# serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
    quest = int(input("Digite um valor: "))
    

    if quest in lista:
        print("valor já existente na lista")
    else:
        lista.append(quest)

    quest2 = input("Quer continuar? [S/N]: ")

    if quest2.upper() == "N":
        break


lista.sort()
print(f"Você digitou os valores {lista}")