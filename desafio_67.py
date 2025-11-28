# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    print("-------------------------------------------")
    inp = int(input("Digite um número para ver sua tabuada: ",)) 
    
    
    if inp < 0:
        break
    else:
        print("\n-------------------------------------------\n")
        print(f" {inp} X 1 = {inp * 1}\n {inp} X 2 = {inp * 2}\n {inp} X 3 = {inp * 3}\n {inp} X 4 = {inp * 4}\n {inp} X 5 = {inp * 5}\n {inp} X 6 = {inp * 6}\n {inp} X 7 = {inp * 7}\n {inp} X 8 = {inp * 8}\n {inp} X 9 = {inp * 9}\n {inp} X 10 = {inp * 10}")
        print("\n-------------------------------------------")

print("Obrigado por testar essse programa, volte sempre!!!")    