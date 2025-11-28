#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um 
#terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    a = l * c
    return a

print("CONTROLE DE TERRENOS")
print("-"*30)

altura = float(input("Digite a largura do terreno (m): "))
comprimento = float(input("Digite a comprimento do terreno (m): "))

print("-"*30)

print(f"A área do terreno é de {area(altura,comprimento)} m²")