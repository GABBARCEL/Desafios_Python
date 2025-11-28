# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º valor: "))

    if len(lista) == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista) and num > lista[pos]:
            pos += 1
        lista.insert(pos, num)

print(f"\nLista ordenada: {lista}")