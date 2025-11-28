# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from moeda import *

Valor = float(input("Digite o preço:\nR$"))
print("´^~-.-~^´" * 16)

print(f"A matade de R${Formatar(Valor)} é R${Metade(Valor, formato=True)}")
print(f"O dobro de R${Formatar(Valor)} é R${Dobro(Valor, formato=True)}")
print(f"Aumentando 10%, temos R${Aumentar(Valor, formato=True)}")
