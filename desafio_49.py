# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input("digite um número para ver sua tabuada: "))

for n in range(1, 11):
    print(f"{n} X {num} = {num * n}")