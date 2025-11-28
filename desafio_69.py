# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário se quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

mans = 0
wm18 = 0
m18 = 0


while True:
    print("=-=-=-=-=-=-=-=-=-=-=-=-")
    print("CADASTRO DE PESSOAS")
    print("=-=-=-=-=-=-=-=-=-=-=-=-")

    idade = int(input("idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()
    cntr = str(input("você quer continuar? [S/N]: ")).strip().upper()

    if idade >= 18:
        m18 += 1
    if sexo == "M":
        mans += 1
    if sexo == "F" and idade < 20:
        wm18 += 1
    
    if cntr == "N":
        break


print(f"há {m18} pessoas maiores de 18 anos\nhá {mans} homens \nhá {wm18} mulheres menores de 20 anos")