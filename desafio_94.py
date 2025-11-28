# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada 
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

lista_pessoas = []
soma = 0
womans = []
p_acmedia = []


veref = 0
while veref == 0:
    pessoa = {}
    pessoa["nome"] = input("Nome:")

    while True:
        pessoa["sexo"] = input("Sexo [M/F]: ").upper()
        
        if pessoa["sexo"] == "M" or pessoa["sexo"] == "F":
            if pessoa["sexo"] == "F":
                womans.append(pessoa["nome"])
            break
        print("[ERRO]! Digitar somente M ou F!")

    pessoa["idade"] = int(input("Idade: "))
    soma += pessoa["idade"]

    lista_pessoas.append(pessoa)

    while True:
        ctg = input("Quer continuar [S/N]:").upper()
        if ctg == "N":
            veref = 1
            break
        elif ctg == "S":
            break
        elif ctg not in "NSns":
            print("[ERRO]! Digite apenas S ou N!")

print(f"{len(lista_pessoas)} pessoas foram cadastradas")
print(f"A média de idade é {soma / len(lista_pessoas)} anos")
print(f"A lista de mulheres são: {womans}")
print("As pessoas com idade acima da média são:")
for p in lista_pessoas:
    if p["idade"] > (soma / len(lista_pessoas)):
        print(f"Nome: {p['nome']}, Idade: {p['idade']}")