# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

tabela = (
    "Flamengo",
    "Palmeiras",
    "Cruzeiro",
    "Bahia",
    "Botafogo",
    "Mirassol",
    "São Paulo",
    "Red Bull Bragantino",
    "Fluminense",
    "Ceará",
    "Corinthians",
    "Atlético Mineiro",
    "Internacional",
    "Vasco da Gama",
    "Santos",
    "Vitória",
    "Juventude",
    "Fortaleza",
    "Recife",
    "Sport",
    "Chapecoense"
)

print(f"os 5 primeiros colocados: {tabela[0:6]}")
print(f"os 4 ultimos colocados: {tabela[-5:]}")
print(f"em ordem alfabética: {sorted(tabela)}")
print(f"posição na tabela: {tabela.index("Chapecoense")}")
