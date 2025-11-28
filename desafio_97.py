#Faça um programa que tenha uma função chamada escreva(), 
#que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(text):
    print("~~" + "~" * len(text) + "~~")
    print("  " + text)
    print("~~" + "~" * len(text) + "~~")


escreva("PNEUMOULTRAMICROSCOPICOSSILICULVULCANOCONIOTICO")