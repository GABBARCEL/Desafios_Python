#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao 
#serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

nasci = int(input("Seu ano de nascimento: "))
idade = 2025 - nasci

print(f"você tem {idade} anos")

if idade == 18:
    print(f"deve se alistar hoje")
elif idade != 18:
    if idade < 18:
        print(f"você deve se alistar daqui {18 - idade} anos")
    elif idade > 18:
        print(f"você se alistou faz {idade - 18} anos")
else:
    print("ERRO")
