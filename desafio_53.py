# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

word = str(input("digite a palavra/frase: "))
format_word = word[::-1].replace(" ", "")


print(f"a palavra {word.lower()}, ao contrário fica {format_word.lower()}")
if format_word.lower() == word.lower().replace(" ", ""):
    print("é um palíndromo")
else:
    print("não é um palíndromo")