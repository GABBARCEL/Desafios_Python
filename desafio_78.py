# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

for q in range(0,5):
    quest = int(input(f"Digite o valor {q}: "))
    lista.append(quest)

pos_maior = []
for i in range(len(lista)):
    if lista[i] == max(lista):
        pos_maior.append(i)

# Encontrar todas as posições do menor valor
pos_menor = []
for i in range(len(lista)):
    if lista[i] == min(lista):
        pos_menor.append(i)

print(30 * "~=")
print(f"você digitou os valores: {lista}")
print(f"O maior valor digitado foi {max(lista)} nas posições {pos_maior}")
print(f"O menor valor digitado foi {min(lista)} nas posições {pos_menor}")