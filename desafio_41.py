# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

nasci = int(input("data de nascimento: "))
idade = 2017 - nasci

print(f"a idade do atleta é {idade}")

if idade <= 9:
    print("classificação: MIRIM")
elif idade > 9 and idade <= 14:
    print("classificação: INFANTIL")
elif idade > 14 and idade <= 19:
    print("classificação: JÚNIOR")
elif idade > 19 and idade <= 25:
    print("classificação: SÊNIOR")
else:
    print("classificação: MASTER")