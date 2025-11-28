#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
#Seu programa tem que realizar três contagens através da função criada


from time import sleep


    # contador normal

def contador(inicil, fim, passo):
#organização para eu não elouquecer
    real_fim = fim
    # EMPEDINDO O USUÁRIO DE COLOCAR PASSO 0
    if passo == 0:
        print("Não é possível fazer uma contagem com passo 0")
        return


    #EMPEDINDO O USUÁRIO DE FAZER UMA CONTAGEM CRESCENTE COM PASSO NEGATIVO
    if passo < 0 and inicil < fim:
        passo = abs(passo)
        

    #EMPEDINDO O USUÁRIO DE FAZER UMA CONTAGEM DECRESCENTE COM PASSO POSITIVO
    elif passo > 0 and inicil > fim:
        passo = -abs(passo)
    
    #CORRIGINDO O RANGE INCOMLETO EM CASO DE PASSO CONTAGEM CRESCENTE
    if passo > 0:
        fim = fim + 1

    #CORRIGINDO O RANGE INCOMLETO EM CASO DE PASSO CONTAGEM DECRESCENTE
    else:
        fim = fim - 1 


    #MENSAGEMZINHA DE CONTADOR
        #EM CASO DE FIM POSITIVO
    print(f"Contagem de {inicil} até {real_fim} de {abs(passo)} em {abs(passo)}")

    for i in range(inicil, fim, passo):
        print(i, "", end="", flush=True)
        sleep(0.5)
    

contador(1, 10, 1)
print("")
contador(10, 0,-2)
print("")

inp_ini = int(input("Inicil: "))
inp_fim = int(input("Fim: "))
inp_passo = int(input("Passo: "))

contador(inp_ini, inp_fim, inp_passo)