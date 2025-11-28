# Aprimore o desafio 93 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
time = []
veref = 0
while veref == 0:
    jogador = {
        "nome": input("Digite o nome do jogador: "),
        "jogos": int(input(f"Digite quantos jogos ele jogou: ")),
        "gols": [],
        "total_gols": 0
    }
    for i in range(1, (jogador["jogos"] + 1)):
        temp_gol = int(input(f"Quantos gols {jogador['nome']} fez no {i}° jogo?\n-"))
        jogador["gols"].append(temp_gol)
        jogador["total_gols"] += temp_gol
    time.append(jogador)
    while True:
        qst = input("Gostaria de adicionar outro jogador [S/N]?\n-").upper()
        if qst == "N":
            veref = 1
            break
        elif qst == "S":
            break
        elif qst not in "SsNn":
            print("[ERRO]! DIGITE APENAS S OU N!")
print("cód.  nome       gols      total")
print("_"*60)
for k, j in enumerate(time):
    print(f"{k}   {j["nome"]:>8}  {j["gols"]}     {j["total_gols"]}")
print("_"*60)
while True:
    busca = int(input("Digite o código do jogador para fazer o levantamento (999 para sair): "))
    if busca == 999:
        break
    if busca not in range(len(time)):
        print("[ERRO] NÃO EXISTE JOGADOR COM ESSE CÓDIGO")
    else:
        print(f"Levantamento do jogador: {time[busca]["nome"]}")
        for i, g in enumerate(time[busca]["gols"]):
            print(f"No jogo {i+1} fez {time[busca]["gols"][i]}")
print("FINALIZANDO...")