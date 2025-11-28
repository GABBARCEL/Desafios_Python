# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

#PARTE SECUNDARIA
def Maior(*numbers):
    print("=-=" * 30)   
    if len(numbers) == 0:
        print("nenhum valor passado\nImposivel determinar o maior valor")
        return

    if len(numbers) == 1:
        maior = numbers[0]
    else:
        maior = max(numbers)
    
    
    print("=-=" * 30)
    print("Analizando os números passados...")
    for i in numbers:
        print(i, "", end = "")
    print(f"\nForam informados {len(numbers)} números ao todo.\nO maior foi {maior}")

#PARTE PRINCIPAL
Maior(2, 9, 4, 5, 7, 1)
Maior(4, 7, 0)
Maior(1, 2)
Maior(6)
Maior()