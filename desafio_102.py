# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o 
# número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado 
# ou não na tela o processo de cálculo do fatorial.

def Fatorial(number, show=False):
    """
    -> Calcula o fatorial do número requisitado
    :param number: Número requisitado para o calculo de fatorial
    :param show: Bollean para visualizar o calculo. True para vizualizar, e false para não. Caso não coloque esse parametro, ele é por padrão setado como false
    :return: Retorna o resultado fatorial, indenpendente do modo show
    """
    
    
    fatorial = 1
    for i in range(number, 0, -1):
        fatorial *= i
        if show == True:
            
            print(i, end = "")
            if i > 1:
                print(" X ", end = "")
            else:
                print(" = ", end = "")
    return fatorial
        


print(Fatorial(5))