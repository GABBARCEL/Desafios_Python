#faça um programa que leia um número qualquer e mostre o seu fatorial
#ex 5! = 5x4x3x2x1 = 120

op = int(input("digite um número: "))
f = 1


c = op
while c > 0:
    f = f * c
    c -= 1

print(f"{op}! = {f}")