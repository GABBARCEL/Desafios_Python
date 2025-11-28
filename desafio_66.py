# crie um programa que leia vários números inteiros pelo teclado. o programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# no final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

lista = []

while True:
    entrada = int(input("Digite um número inteiro, ou 999 para encerrar: "))

    if entrada == 999:
        break
    else:
        lista.append(entrada)

        
print(f"você digitou {len(lista)} e a soma deles é {sum(lista)}")