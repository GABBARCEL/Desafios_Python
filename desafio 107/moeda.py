def Aumentar(valor, porcentagem = 10):
    """
    -> Calcula o valor fornecido com uma porcentagem a mais (caso não seja fornecida, será acrescentado 10%)
    :param valor: Valor a ser fornecido como base para o calculo
    :param porcentagem: Porcentagem a ser calculada e adicionada ao valor total
    :return: Retorna o valor inicial + o valor percentual calculado
    """
    total = valor + (valor / 100 * porcentagem)
    return total


def Diminuir(valor, porcentagem = 10):
    """
    -> Calcula e retorna o valor fornecido com uma porcentagem a menos (caso não seja fornecida, será acrescentado 10%)
    :param valor: Valor a ser fornecido como base para o calculo
    :param porcentagem: Porcentagem a ser calculada e subtraí ao valor total
    :return: Retorna o valor inicial - o valor percentual calculado
    """
    total = valor + (valor / 100 * porcentagem)
    return total


def Dobro(valor):
    """
    -> Calcula o dobro do valor fornecido e retorna
    :param valor: Valor a ser fornecido para multiplicalo por 2
    :return: Retorna o dobro do valor fornecido
    """
    total = valor * 2
    return total


def Metade(valor):
    """
    -> Calcula a metade do valor fornecido e retorna
    :param valor: Valor a ser fornecido para dividivo por 2
    :return: Retorna a metade do valor fornecido
    """
    total = valor / 2
    return total