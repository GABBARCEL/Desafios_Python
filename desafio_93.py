# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols 
# feitos durante o campeonato.

# 1
print()
jogador = {
    "nome": input("Digite o nome do jogador: "),
    "jogos": int(input(f"Digite quantos jogos ele jogou: ")),
    "gols": [],
    "total_gols": 0
}


# 1.9
for i in range(1, (jogador["jogos"] + 1)):
    temp_gol = int(input(f"Quantos gols {jogador['nome']} fez no {i}° jogo?\n-"))
    jogador["gols"].append(temp_gol)
    jogador["total_gols"] += temp_gol

# 2.1
print("=-" * 30)
print(jogador)

# 2.2
print("=-" * 30)
for k, v in jogador.items():
    print(f"O campo {k} tem valor {v}")

# 2.3
print("=-" * 30)
print(f"O jogador {jogador["nome"]} jogou {jogador['jogos']} jogos:")

for i, v in enumerate(jogador["gols"]):
    print(f"    =>Na partida {i + 1}, fez {v} gol")

print(f"O total de gols foi de: {jogador['total_gols']}")