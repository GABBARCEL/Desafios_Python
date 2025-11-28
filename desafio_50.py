# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

lista_fora = 0
cont = 0

for n in range(1,7):
    num = int(input("digite um número: "))
    if num % 2 == 0:
        lista_fora += num
        cont += 1
print(f"você informou {cont} números pares, a soma deles é {lista_fora}")