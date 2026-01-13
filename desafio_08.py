# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input("Digite a medida em metros, a ser calculada: "))

centimetros = metros * 100
milimetros = centimetros * 100

print(f"{metros} metros em centimentros são: {centimetros}\n{metros} metros em milimetros são: {milimetros}")