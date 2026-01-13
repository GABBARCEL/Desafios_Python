# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

entrada = float(input("Digite a temperatura em ºC:"))

F = (entrada * 1.8) + 32

print(f"{entrada}ºC em ºF fica: {F}ºF")