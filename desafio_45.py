# Crie um programa que faça o computador jogar Jokenpô com você.

import secrets as sc
import time as tm

jogaveis = {0 : "pedra" , 1 : "papel", 2 : "tesoura"}


CPU_PLAY = sc.choice(jogaveis)

print("Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA")

pl_jogada = int(input("Sua jogada: "))

if CPU_PLAY == jogaveis[0] and pl_jogada == 2:
    det =+ 1
elif CPU_PLAY == jogaveis[1] and pl_jogada == 0:
    det =+ 1
elif CPU_PLAY == jogaveis[2] and pl_jogada == 1:
    det =+ 1
elif CPU_PLAY == jogaveis[0] and pl_jogada == 1:
    det =- 1
elif CPU_PLAY == jogaveis[2] and pl_jogada == 1:
    det =- 1
elif CPU_PLAY == jogaveis[1] and pl_jogada == 2:
    det =- 1
elif CPU_PLAY == jogaveis[2] and pl_jogada == 0:
    det =- 1
elif CPU_PLAY == jogaveis[0] and pl_jogada == 0:
    det = 0
elif CPU_PLAY == jogaveis[1] and pl_jogada == 1:
    det = 0
elif CPU_PLAY == jogaveis[2] and pl_jogada == 2:
    det = 0

#jo ke po
print("JO")
tm.sleep(0.5)
print("KEN")
tm.sleep(0.5)
print("PÔ")
tm.sleep(1)
if det == -1:
    print(f"a máquina jogou {CPU_PLAY}, você ganhou!")
elif det == 1:
    print(f"a máquina jogou {CPU_PLAY}, você perdeu!")
elif det == 0:
    print(f"a máquina também jogou {CPU_PLAY}, vocês empataram!")