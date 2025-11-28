# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = []

contador = 0

entry = input("Digite uma expressão: ")

for i in entry:
    if i == "(":
        contador += 1
    elif i == ")":
        contador -= 1

if contador == 0:
    Certo = "correta"
else:
    Certo = "errada"


print(f"A sua expressão está {Certo}")