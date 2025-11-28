# escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de converção:
# 1 para base binário, 2 para octal e 3 para hexadecimal

INPUT = int(input("escreva um número inteiro para ser convertido: "))
comand = int(input("DIGITE:\n[1] para binário\n[2] para octal \n[3] para hexadecimal\nENTRADA:"))

if comand == 1:
    print(f"{INPUT} converteu-se em: {bin(INPUT)[2:]}")
elif comand == 2:
    print(f"{INPUT} converteu-se em: {oct(INPUT)[2:]}")
elif comand == 3:
    print(f"{INPUT} converteu-se em: {hex(INPUT)[2:]}")
else:
    print("comando inválido")