# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


import random as rd

sort1 = rd.randint(1,10)
sort2 = rd.randint(1,10)
sort3 = rd.randint(1,10)
sort4 = rd.randint(1,10)
sort5 = rd.randint(1,10)

tupla = (sort1,sort2, sort3, sort4, sort5)

print(f"5 números aleatórios: {tupla}")
print(f"o maior número é o {max(tupla)}, e o menor é {min(tupla)}")
