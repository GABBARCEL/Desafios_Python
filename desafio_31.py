# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
# cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.

distancia = float(input("Quantos Km tem até o destino?"))
if distancia < 200:
    preco = distancia * 0.50
elif distancia > 200:
    preco = distancia * 0.45

print(f"O preço de sua viagem será de R${preco}")