# Crie um programa que leia o nome completo de uma pessoa e mostre:

# > O nome com todas as letras maiúsculas e minúsculas.
# > Quantas letras ao todo (sem considerar espaços).
# > Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: ")).strip()
separa = nome.split()
print("Analisando seu nome...")
print(f"Seu nome em maiúsculas é {nome.upper()}.")
print(f"Seu nome em minúsculas {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome) - nome.count(" ")}")
print(f"Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras.")