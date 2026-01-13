# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite o seu salário: R$"))

aumento = salario / 100 * 15

print(f"O seu novo salário será de: R${salario+aumento}")