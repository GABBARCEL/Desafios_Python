#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota1 = float(input("nota 1: "))
nota2 = float(input("nota 2: "))
média = (nota1 + nota2) / 2

print(f"sua média é de {média}")

if média >= 7:
    print("APROVADO")
elif média >= 5 and média <= 6.9:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")
