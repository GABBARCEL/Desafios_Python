#faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'm' ou 'f'. peça 
# a digitação novamente até ter um valor correto

c = 1

while c != 0:
    quest = str(input("qual o seu sexo? [M/F] ")).strip()
    if quest in "Ff" or quest in "Mm":
        c -= 1
    print("opão inválida, tente novamente:")
print("FIM")