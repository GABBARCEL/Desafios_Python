# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos 
# pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

Matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        Matriz[l][c] = int(input(f"Digite o valor para {l, c}"))
        

for l in range(0,3):
    print(Matriz[l])
