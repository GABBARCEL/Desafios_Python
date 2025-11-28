#  Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

lista_menor = []
lista_maior = []

for c in range(1, 8):
    nasci = int(input(f"data de nascimento da {c}° pessoa: "))
    age = 2025 - nasci
    if age >= 18:
        lista_maior.append(age)
    else:
        lista_menor.append(age)

print(f"{len(lista_menor)} pessoas são menores de 18 anos")
print(f"{len(lista_maior)} pessoas são maiores de 18 anos")
