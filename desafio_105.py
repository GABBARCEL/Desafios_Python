# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas– 
# A maior nota 
# A situação (opcional)

def Notas(*notas, sit = False):
    média = sum(notas) / len(notas)
    
    geral = {}

    if sit == True:
        if média >= 6 and média < 8:
            situação = "OK"
        elif média >= 8:
            situação = "òtima"
        elif média < 6:
            situação = "Ruim"
        geral = {
            'total de notas' : len(notas),
            'maior nota' : max(notas),
            'menor nota' : min(notas),
            'média' : média,
            'situação atual' : situação
        }
    

    else:
        geral = {
            'total de notas' : len(notas),
            'maior nota' : max(notas),
            'menor nota' : min(notas),
            'média' : média
        }


    return geral

n = Notas(5,9,7,8, sit = True)
print(n)