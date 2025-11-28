# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random as rd
won = 0

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("VAMOS JOGAR PAR OU ÍMPAR!")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n \n")

while True:
    
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    BOT = rd.choice(range(1,10))
    print(BOT)
    inp = input("Par ou ímpar? [P/I]: ").upper()
    nmb = int(input("Jogue seu número: ")) 


    if inp == "P":
        if (nmb + BOT) % 2 ==  0:
            print("você ganhou!")
            won += 1
        else:
            print("você perdeu...")
            break        
    
    elif inp == "I":
        if (nmb + BOT) % 2 !=  0:
            print("você ganhou")
            won += 1
        else:
            print("você perdeu...")
            break
    
    else:
        print("caracter inválido, digite apenas P ou I !")


print("OBRIGADO POR JOGAR!!!")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(f"você ganhou {won} vezes!")