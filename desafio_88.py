# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 
# 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint

print("=-=" * 30)
print("MEGA SENA")
print("=-=" * 30)

qst = int(input("Quantos jogos deseja jogar? "))

for n in range(1, qst + 1):
    jogo = []
    while len(jogo) < 6:
        num = randint(1,60)
        if num not in jogo:
            jogo.append(num)
            
    print(jogo)