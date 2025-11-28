# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ("cachorro", "gato", "armário", "ganso", "mesa", "cadeira", "notebook", "vscode", "python", "desenvolvimento")

for i in palavras:
    vogais = []
    for c in i:
        if c.upper() in "AEIOU":
            vogais.append(c)    
    print(f"\nna palavra {i.upper()}, temos as vogais: {vogais}", end="")