# Faça um programa que leia nome e média de um aluno, guardando também a situação 
# em um dicionário. No final, mostre o conteúdo da estrutura na tela

nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    situacao = "Aprovado"
elif nota < 7 and nota > 5:
    situacao = "recuperação"
elif nota < 5:
    situacao = "Reprovado"

status = {
    "Nome": nome,
    "Nota": nota,
    "Situação": situacao
}

print("=-" * 26)
print(f"Nome: {status['Nome']}\nMédia: {status['Nota']}\nSituação: {status['Situação']}")