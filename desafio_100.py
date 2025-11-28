# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep

numeros = []
pares = []
                
# Funções
    # FUNÇÃO DE SORTEAR E COLOCAR NA LISTA DE NÚMEROS
def Sorteia(lista):
    for i in range(0,5):
        lista.append(randint(1,10))
        print(lista[i], " ", end = "", flush=True)
        sleep(0.5)
    print("PRONTO")


    # FUNÇÃO SEPARAR E SOMAR OS NÚMEWROS PARES
def SomaPar(entrada):
    for i in entrada:
        if i % 2 == 0:
            pares.append(i)
    sleep(0.5)
    print(f"Os números pares são: {" ".join(map(str, pares))}")
    print(f"A soma dos números pares sorteados são: {sum(pares)}")


# Chamar as funções
Sorteia(numeros)
SomaPar(numeros)