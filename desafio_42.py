# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

seg1 = int(input("qual o primeiro segmento: "))
seg2 = int(input("qual o segundo segmento: "))
seg3 = int(input("qual o terceiro segmento: "))

if seg1 + seg2 > seg3 and seg2 + seg3 > seg1 and seg3 + seg1 > seg2:
    print("TRIÂNGULO POSSÍVEL!")
    if seg1 == seg2 and seg2 == seg3:
        print("é um triângulo EQUILÁTERO")
    elif seg1 != seg2 and seg2 != seg3 and seg1 != seg3:
        print("é um triângulo ESCALENO")
    else:
        print("é um triângulo ISÓSCELES") 
else:
    print("triângulo IMPOSSÍVEL")