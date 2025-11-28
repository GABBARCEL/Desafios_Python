# crie um programa que leia vários números inteiros pelo teclado. o programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. no final, mostre quantos números foram digitados e quaç a sema entre eles(desconsiderando o flag)

list_sum = []

c = 0
while c < 1:
    tent = int(input("[999 PARA PARAR]\n[NÚMERO QUALQUER]: "))
    if tent == 999:
        c = 1
    else:
        list_sum.append(tent)

print(f"você digitou {len(list_sum)}, a soma entre eles foi de {sum(list_sum)}")
