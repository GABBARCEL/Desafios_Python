def Aumentar(valor, porcentagem = 10, formato=False):
    """
    -> Calcula o valor fornecido com uma porcentagem a mais (caso não seja fornecida, será acrescentado 10%)
    :param valor: Valor a ser fornecido como base para o calculo
    :param porcentagem: Porcentagem a ser calculada e adicionada ao valor total
    :param formato: Diz a função se deve retornar um valor formatado para moeda
    :return: Retorna o valor inicial + o valor percentual calculado
    """
    total = valor + (valor / 100 * porcentagem)
    
    if formato:
        return f"{total:.2f}".replace('.', ',')
    else:
        return total


def Diminuir(valor, porcentagem = 10, formato=False):
    """
    -> Calcula e retorna o valor fornecido com uma porcentagem a menos (caso não seja fornecida, será acrescentado 10%)
    :param valor: Valor a ser fornecido como base para o calculo
    :param porcentagem: Porcentagem a ser calculada e subtraí ao valor total
    :param formato: Diz a função se deve retornar um valor formatado para moeda
    :return: Retorna o valor inicial - o valor percentual calculado
    """
    total = valor - (valor / 100 * porcentagem)

    if formato:
        return f"{total:.2f}".replace('.', ',')
    else:
        return total


def Dobro(valor, formato=False):
    """
    -> Calcula o dobro do valor fornecido e retorna
    :param valor: Valor a ser fornecido para multiplicalo por 2
    :param formato: Diz a função se deve retornar um valor formatado para moeda
    :return: Retorna o dobro do valor fornecido
    """
    total = valor * 2

    if formato:
        return f"{total:.2f}".replace('.', ',')
    else:
        return total


def Metade(valor, formato=False):
    """
    -> Calcula a metade do valor fornecido e retorna
    :param valor: Valor a ser fornecido para dividivo por 2
    :param formato: Diz a função se deve retornar um valor formatado para moeda
    :return: Retorna a metade do valor fornecido
    """
    total = valor / 2

    if formato:
        return f"{total:.2f}".replace('.', ',')
    else:
        return total
    

def Formatar(valor):
    """
    -> Formata para padrão brasileiro de moeda. Importante ressaltar que RETORNA COMO STRING!
    :valor: Valor a ser formatado
    :return: String com o valor de entrada formatado para o padrão brasileiro (sem o R$ ou $)
    """
    texto_formatado = f"{valor:.2f}".replace(".",",")
    return texto_formatado


def Resumo(entrada, aumento, reducao):
    print("´^~^`" * 9)
    print(" " * 14, "RESUMO DO VALOR")
    print("´^~^`" * 9)
    print(f"Preço analizado:     ", f"R${Formatar(entrada)}")
    print(f"Dobro do Preço:      ", f"R${Dobro(entrada, formato=True)}")
    print(f"Metade do preço:     ", f"R${Metade(entrada, formato=True)}")
    print(f"{aumento}% de aumento:      ", f"R${Aumentar(entrada, aumento, formato=True)}")
    print(f"{reducao}% de redução:      ", f"R${Diminuir(entrada, reducao, formato=True)}")

