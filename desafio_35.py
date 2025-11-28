# desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

seg1 = int(input("qual o primeiro segmento: "))
seg2 = int(input("qual o segundo segmento: "))
seg3 = int(input("qual o terceiro segmento: "))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print("TRIÂNGULO IMPOSSÍVEL!")
else:
    print("as retas podem gerar um triângulo!")