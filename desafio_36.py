###escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. o programa vai perguntar o valor da casa, o salário do
#do comprador e em quantos anos ele vai pagar.

###CALCULE O VALOR DA PRESTAÇÃO MENSAl, SABENDO QUE ELA NÃO PODE EXCEDER 30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO!

salario = float(input("qual o seu salário? "))
valor = float(input("qual o valor que precisa? "))
anos = int(input("quantos anos será o financiamento? "))


parcela = float(valor / (anos * 12))
porcentagem = float(salario * 30 / 100)

if porcentagem < parcela:
     print(f"financiamento negado, motivo: salário abaixo dos 30% exigido (atual: {porcentagem:.2f} exigido: {salario + porcentagem:.2f})") 
elif parcela <= salario:
     print(f"financiamento aprovado, maus parabéns pela sua descisão!")
     print(f"a parcela será: {parcela:.2f}, durante {anos} anos")
else:
     print("ERRO: CONTATE A EQUIPE TECNICA PARA RESOLVER SEU PROBLEMA")