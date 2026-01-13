# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar.
# Considere U$ 1,00 = R$ 3,27

carteira = float(input("Digite o valor que você tem na carteira: "))

print(f"Você pode comprar U$D {carteira // 3.27}")