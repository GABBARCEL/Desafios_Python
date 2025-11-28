# #escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
# o primeiro é maior
# o segundo é maior
# os números são iguais

ENTRADA1 = int(input("digite o primeiro número: "))
ENTRADA2 = int(input("digite o segundo número: "))

if ENTRADA1 == ENTRADA2:
    print("são números iguais")
elif ENTRADA1 != ENTRADA2:
    if ENTRADA1 > ENTRADA2:
        print(f"{ENTRADA1} é maior que {ENTRADA2}")
    if ENTRADA1 < ENTRADA2:
        print(f"{ENTRADA1} é menor que {ENTRADA2}")
else:
    print("erro")
