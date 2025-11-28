# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os 
# em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.

Numeros = [[],[]]

for i in range(1, 8):
    n = int(input(f"Digite o {i}° número:\n"))

    if n % 2 == 0:
        Numeros[0].append(n)
    else:
        Numeros[1].append(n)

    Numeros[0].sort()
    Numeros[1].sort()
    

print(f"Os valores pares são: {Numeros[0]}\nOs valores ímpares são: {Numeros[1]}")