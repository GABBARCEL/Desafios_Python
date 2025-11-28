# Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

def SelectHelp(SearchArg):
    while True:
        print("""

 ██░ ██▓█████ ██▓    ██▓███           ██▓███▓██   ██▓                                                                                 
▓██░ ██▓█   ▀▓██▒   ▓██░  ██▒        ▓██░  ██▒██  ██▒
▒██▀▀██▒███  ▒██░   ▓██░ ██▓▒        ▓██░ ██▓▒▒██ ██░
░▓█ ░██▒▓█  ▄▒██░   ▒██▄█▓▒ ▒        ▒██▄█▓▒ ▒░ ▐██▓░
░▓█▒░██░▒████░██████▒██▒ ░  ░    ██▓ ▒██▒ ░  ░░ ██▒▓░
 ▒ ░░▒░░░ ▒░ ░ ▒░▓  ▒▓▒░ ░  ░    ▒▓▒ ▒▓▒░ ░  ░ ██▒▒▒ 
 ▒ ░▒░ ░░ ░  ░ ░ ▒  ░▒ ░         ░▒  ░▒ ░    ▓██ ░▒░ 
 ░  ░░ ░  ░    ░ ░  ░░           ░   ░░      ▒ ▒ ░░  
 ░  ░  ░  ░  ░   ░  ░             ░          ░ ░     
                                  ░          ░ ░     
      """)
        print("""
▄▄▄▄   ▄▄▄  ▄▄▄▄     ▄████   ▄▄▄  ▄▄▄▄  ▄▄▄▄   ▄▄▄  ▄▄▄▄   ▄▄▄▄ ▄▄▄▄▄ ▄▄    
██▄█▀ ██▀██ ██▄█▄   ██  ▄▄▄ ██▀██ ██▄██ ██▄██ ██▀██ ██▄█▄ ██▀▀▀ ██▄▄  ██    
██    ▀███▀ ██ ██    ▀███▀  ██▀██ ██▄█▀ ██▄█▀ ██▀██ ██ ██ ▀████ ██▄▄▄ ██▄▄▄ 
""")
        
        print("`^~-._.-~^´" * 33)
        
        inp = input("Digite o nome da biblioteca ou comando para obter ajuda. Ou digite FIM, para sair:\n-")

        if inp.upper() == "FIM":
            break
        else:
            print("`^~-._.-~^´" * 30)
            help(inp)
            print("`^~-._.-~^´" * 30)
    print("Finalizando...")

SelectHelp("Time")