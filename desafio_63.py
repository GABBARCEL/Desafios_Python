# escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros 
# elementos de uma sequência fibonacci
# ex: 0 1 1 2 3 5 8

n = int(input("quantos termos: "))

t1 = 0
t2 = 1

print(t1,"->",t2, end = "")

cont = 3
while cont <= n:
    t3 = t1 + t2
    print("", "->",t3, end="")
    t1 = t2
    t2 = t3
    cont += 1
print("-> fim")