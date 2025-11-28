# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def Ficha(jogador="", gols=0):
    if jogador.strip() == "":
        jogador = "<DESCONHECIDO>"
    
    print(f"O jogador {jogador}, fez {gols} gols no campeonato.")


Jogador= input("Digite o nome do jogador: ")
Gols= input("Quantos gols ele marcou no campeonato: ")
if Gols.isnumeric():
    Gols = int(Gols)
else:
    Gols = 0



Ficha(Jogador,Gols)