# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) 
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de 
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

# 1
pessoa = {
    "nome": input("Digite seu nome:"),
    "ano": int(input("Digite seu ano de nascimento:"))
}

# 2
ctps = int(input("Digite o número da CTPS (ou 0 caso não tenha): "))

# 2.5
if ctps != 0:
    pessoa["ctps"] = ctps
    cntc = int(input("Digite o ano de contratação: "))
    salario = float(input("Digite se salário: R$"))
    pessoa["cntc"] = cntc
    pessoa["salario"] = salario

# 3
print("-=" * 30)
print(f"O NOME CADASTRADO FOI: {pessoa['nome']}\nA IDADE CADASTRADA FOI: {2025 - pessoa['ano']}")

# 3.1
if ctps != 0:
    print(f"O CTPS CADASTRADO FOI: {ctps}\nO SALÁRIO CADASTRADO FOI: R${pessoa['salario']}\nO ANO DE CONTRATAÇÃO CADASTRADO FOI: {cntc}\nO ANO DE APOSENTSADORIA ESTÁ PREVISTO PARA {pessoa['cntc']+35}, FALTANDO {(pessoa['cntc']+35) - 2025} anos.")
