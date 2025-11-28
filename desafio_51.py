# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input("o primeiro termo: "))
prog = int(input("progressão: "))
decimo = termo + (11 - 1) * prog

for n in range(termo, decimo, prog):
    print(f"{n} ", end = "→ "  )
print("FIM")