# Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
#     A) Quantas pessoas foram cadastradas.
#         B) Uma listagem com as pessoas mais pesadas.
#             C) Uma listagem com as pessoas mais leves.

temp = []
princi = []
min = men = 0

while True:
    temp.append(input("Digite seu nome:\n"))
    temp.append(float(input("Digite seu peso:\n")))
    
    if len(princi) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    
    princi.append(temp[:])
    temp.clear

    resp = input("que continuar?\nS/N]:")
    if resp in "Nn":
        break

print(f"Você cadastrou {len(princi)} pessoas.")
print(f"a o maior peso foi {mai}Kg. peso de ", end = "")

for p in princi:
    if p[1] == mai:
        print(f"[{p[0]}]", end = "")

print()
print(f"O menor peso foi de {men}Kg. peso de ", end="")
for p in princi:
    if p[1] == men:
        print(f"[{p[0]}]", end="")
print()