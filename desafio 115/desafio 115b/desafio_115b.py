from veref import *
from cadastros import *
from time import sleep


opcoes = ["Visualizar pessoas cadastradas;", "Cadastrar no sistema", "Sair do sistema"]
archive = "_ListaCadastrados.txt"

while True:
    if Exists(archive):
        sleep(2)
        print("Arquivo de cadastro encontrado com sucesso!!!")
        break
    else:
        print("CRIANDO O ARQUIVO DE CADASTROS...")
        CreateArchive(archive)


Title("Titulo de Teste!!!")
Menu(opcoes)
Input(opcoes, 3, archive)