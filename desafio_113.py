# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def LeiaInt(MensageInput, MensageErro = None):
    while True:
        try:
            Value_local = int(input(MensageInput))

        except:
            print(MensageErro)
            continue
        
        else:
            return Value_local


def LeiaFloat(MensageInput, MensageErro = None):
    while True:
        try:
            Value_local = float(input(MensageInput))

        except:
            print(MensageErro)
            continue
        
        else:
            return Value_local


print(LeiaFloat("entradado número decimal: ", "[ERRO] valor digitado inesperado!"))
print(LeiaInt("entrada do número inteiro:", "[ERRO] valor digitado inesperado!"))