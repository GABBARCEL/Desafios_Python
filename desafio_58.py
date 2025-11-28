# melhore o jogo do desafio 28 onde o compútador vai pensar em um mnúmero entre 0 e 10. só que agora o jogador vai tentar adivinhar 
# até acertar, mostrando no final quantos palpites foram necessários para vencer

from random import randint as rt

sorteio = rt(0,10)
cont = 1

print("escolhi um número entre 0 e 10, adivinhe! ")

c = 0

print(sorteio)

while c == 0:
    tent = int(input("sua tentativa: "))

    if tent == sorteio:
        c += 1
        if cont == 1:
            print("você acerou de primeira!!!")
        else:
          print(f"você ganhou, mas com {cont} palpites")

    else:
        cont += 1
    

print("você ganhou")