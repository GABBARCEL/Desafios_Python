def LeiaDinheiro(mensagem):
    Valido = False
    while Valido==False:
        entrada = input(mensagem).replace(",",".")

        if entrada.isalpha() or entrada.strip() == "":
            print(f"[ERRO] \"{entrada}\" não é um preço válido! ")
        else:
            return float(entrada)
            break
        
      