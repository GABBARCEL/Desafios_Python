# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ("secadora", 1899.9, "panela de pressão", 70, "almofada", 25, "televisão 50' ", 2399.90, "cntg. mesa de jantar", 1500)


print(90 * "=")
print(f"TABELA DE PRODUTOS")
print(90 * "=")

for i in range(len(produtos)):
    if isinstance(produtos[i],str):
        print(f" {produtos[i].strip()} {(50 - len(produtos[i])) * ".".strip()} R${produtos[i + 1]:.2f}")
    else:
        pass


print(90 * "=")