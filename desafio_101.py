# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento 
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def Voto(nascimento):
    idade = 2025 - nascimento
    if idade < 0:
        return idade, "Ano de nascimento inválido"
    
    else:
        if idade >= 16 and idade < 18 or idade > 59:
            return idade, "O voto é opcional"
        
        elif idade >= 18 and idade < 60:
            return idade, "O voto é obrigatório"
        
        elif idade < 16:
            return idade, "O voto é negado"
        

inp = int(input("Digite o ano de nascimento: "))
idade, situacao = Voto(inp)
print("=-=" * 30)


print(f"A idade fornecida é {idade}, {situacao}")