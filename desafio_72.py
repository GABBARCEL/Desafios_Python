# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

nmr = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez" , "onze", "treze", "quatorze", "quinze", "deseseis", "desesete", "desoito", "desenove", "vinte")

i = int(input("Digite um número entre 0 e 20: "))

print(f"o número que voê digitou foi {nmr[i]}")