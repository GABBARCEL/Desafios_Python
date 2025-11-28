#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("digite um número: "))
lista_dv = []
total = 0

for n in range(1, num + 1):
    if num % n == 0:
        lista_dv.append(n)
        total += 1

print(f"lista números divisiveis: {lista_dv}")

if len(lista_dv) > 2:
    print(f"o número {num} não primo, pois ele divide {total} vezes")
elif len(lista_dv) == 2:
        print(f"o número {num} é primo, pois ele divide {total} vezes")