#  Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#  Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário
#  em ordem, sabendo que o vencedor tirou o maior número no dado.
from operator import itemgetter
from random import randint

Joao = randint(1,6)
maria = randint(1,6)
Jose = randint(1,6)
Gustavo = randint(1,6)

results = {
    "Joao": Joao,
    "Maria": maria,
    "Jose": Jose,
    "Gustavo": Gustavo
}

ranking = {}

for k, v in results.items():
    print(f"{k} tirou {v} no dado!")
    
ranking = sorted(results.items(), key = itemgetter(1), reverse = True)

for i, v in enumerate(ranking):
    print(f"{i+1}° lugar: {v[0]} com {v[1]}")