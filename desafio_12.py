# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite o valor do produto: R$"))

desconto = preco / 100 * 5

print(f"O valor total do produto/serviço, era de R${preco}. Com 5% de desconto, ficou R${preco-desconto}")