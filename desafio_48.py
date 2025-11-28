# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
# P.S o resultado é 41583
c = 0
cont = 0

for n in range(1, 501):
    if n % 2 == 0:
        pass
    else:
        if n % 3 == 0:
            c += n
            cont += cont

print(cont, c)