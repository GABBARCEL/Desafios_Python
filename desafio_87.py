# Aprimore o desafio anterior, mostrando no final:
#   A) A soma de todos os valores pares digitados.
#       B) A soma dos valores da terceira coluna.
#           C) O maior valor da segunda linha.

Matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        Matriz[l][c] = int(input(f"Digite o valor para {l, c}"))

        
for l in range(0,3):
    print(Matriz[l])


soma = sum(Matriz[0]) + sum(Matriz[1]) + sum(Matriz[2])
Col_3 = Matriz[0][2] + Matriz[1][2] + Matriz[2][2]


print(f"a soma de todos os valores são: {soma}")
print(f"a soma dos valores da 3° coluna é: {Col_3}")
print(f"o maior valor da 2° linha da matriz é: {max([Matriz[0][1], Matriz[1][1], Matriz[2][1]])}")