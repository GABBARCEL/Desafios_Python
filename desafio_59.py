#crie um programa que leia 2 valores e mostre num menu na tela
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
#seu programa deverá realizar a operação solicitada em cada caso

c = 0

a = 0
b = 0

num1 = int(input("digite o 1° número"))
num2 = int(input("digite o 2° número"))

while c == 0:
    print("=-=-=-=-= MENU =-=-=-=-=\n    [1] SOMAR\n    [2] MULTIPLICAR\n    [3] MAIOR\n    [4] NOVOS NÚMEROS\n    [5] SAIR")
    op = int(input("Sua opção: "))

    if op == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif op == 2:
        print(f"{num1} X {num2} = {num1 * num2}")
    elif op == 3:
        if num1 > num2:
            print(f"{num1} é maior que {num2}")
        elif num1 < num2:
            print(f"{num2} é maior que {num1}")
        else:
            print("os números são iguais")
    elif op == 5:
        print("adeus!")
        c = 1
    elif op == 4:
        num1 = int(input("digite o 1° número"))
        num2 = int(input("digite o 2° número"))
            
