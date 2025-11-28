# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from moeda import *

Valor = float(input("Digite o preço:\nR$"))
print("´^~-.-~^´" * 16)

print(f"A matade de R${Valor:.2f} é R${Metade(Valor)}".replace(".",","))
print(f"O dobro de R${Valor:.2f} é R${Dobro(Valor)}".replace(".",","))
print(f"Aumentando 10%, temos R${Aumentar(Valor)}")
