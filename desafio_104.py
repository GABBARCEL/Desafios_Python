# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
def LeiaInt(inp, ErroMensage = "[ERRO] Digite um número inteiro!"):
    exit = 0
    while True:
        ent = input(inp)
        if ent.isnumeric():
            exit = int(ent)
            break
        else:
            print(ErroMensage)
    return exit
n = LeiaInt("Digite um número: ")
print(f"Você acabou de digitar {n} ")