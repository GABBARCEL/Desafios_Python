# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2 m²

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

parede = largura * altura

print(f"Sua parede mede {altura} x {largura}, totalizando {parede}m².")
print(f"Você precisara de {parede / 2} litros de tinta!")
