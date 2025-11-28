# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

print("~-~-~-~-~-LOJA-~-~-~-~-~\n" \
"FORMAS DE PAGAMENTO:\n" \
"[1] A VISTA DINHEIRO OU PIX (10% DE DESCONTO)\n" \
"[2] A VISTA NO CARTÃO (5% DE DESCONTO)\n" \
"[3] 2X NO CARTÃO\n" \
"[4] 3X OU MAIS NO CARTÃO (20% DE JUROS)\n")

valor = float(input("VALOR A PAGAR: "))
inp = int(input("Sua opção de pagamento: "))

if inp == 1:
    print(f"o valor total a pagar ficou em: R${(valor - valor * 10 / 100):.2f}")
elif inp == 2:
    print(f"o valor total a pagar ficou em: R${(valor - valor * 5 / 100):.2f}")
elif inp == 3:
    print(f"o valor total a pagar ficou em: R${valor:.2f}")
    print(f"O valor total será dividido em 2 parcelas, que terá o valor da parcela será R$({valor / 2}):.2f")
elif inp == 4:
    print(f"o valor total a pagar ficou em: R${(valor + (valor * 20 /100)):.2f}")
    parcelas = int(input("em quantas parcelas será pago? "))
    if parcelas != 1 and parcelas != 2:
        print(f"o valor total será parcelado em {parcelas} vezes, o valor da parcela será de R${((valor + (valor * 20 /100)) / parcelas):.2f}")
    else:
        print("número de parcelas inválida, por favor reinicie o programa")
else:
    print("reinicie o programa e selecione uma opção válido de pagamento")
    