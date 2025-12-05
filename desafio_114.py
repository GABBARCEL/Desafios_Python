# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

from urllib.request import *

url = "https://pudim.com.br"

try:
    urlopen(url)

except:
    print("[ERRO] o site não está acessível no momento.")

else:
    print("OK")