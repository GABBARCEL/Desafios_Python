# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

homem_velho = ""
idade_homem = 0

mulher_nova = 0

idades_md = 0


for p in range(1, 5):
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    nm = str(input(f"qual o nome da {p}º pessoa?"))
    age = int(input(f"qual a idade da {p}º pessoa?"))
    sex = str(input(f"qual o sexo da {p}º pessoa?"))
    
    idades_md += age

    if sex in "Mm":
        if idade_homem == 0:
            homem_velho = nm
            idade_homem = age
        else:
            if age > idade_homem:
                homem_velho = nm
                idade_homem = age
    else:
        if age < 20:
            mulher_nova += 1


if homem_velho != "":
    print(f"o homem mais velho é o {homem_velho}, e ele tem {idade_homem} anos")
else:
    print("não existe homens no grupo")

print(f'a média de idade do grupo é de {idades_md / 4:.1}')
print(f"existem {mulher_nova} mulheres que são menores de 20 anos") 

