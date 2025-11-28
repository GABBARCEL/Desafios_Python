#  crie um programa que leia vários números inteiros pelo teclado. no final da execução,
#  mostre a média entre todos os valores lidos e qual foi os maiores e qual foi o menores lidos.
#  o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

lista_num = []
maior = None
menor = None

while True:
    
    quest = int(input('digite um número: '))
    
    
    lista_num.append(quest)
    

    if maior == None:
        maior = quest
    else:
         if maior < quest:
             maior = quest
    
    if menor == None:
        menor = quest 
    else:
        if menor > quest:
                menor = quest
    
    quest2 = str(input("quer continuar? \n[S/N]: ")).upper().strip()
    
    if quest2 ==  "N":
        break
    

mid = sum(lista_num) / len(lista_num) 
print(f"você digitou {len(lista_num)} números \n A média dentre os números que digitou foi {mid}\n O maior número digitado foi: {maior}\n e o menor foi: {menor}")