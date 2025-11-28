# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

qst1 = int(input("digite um número: "))
qst2 = int(input("digite um número: "))
qst3 = int(input("digite um número: "))
qst4 = int(input("digite o último número: "))

pares = []

tupla = (qst1,qst2,qst3,qst4)

for c in tupla:
    if c % 2 == 0:
        pares.append(c)

print(f"o número 9, apareceu {tupla.count(9)}")
print(f"o número 3, apareceu na posição {tupla.index(3) + 1}")
print(f"os números pares são: {pares}")
