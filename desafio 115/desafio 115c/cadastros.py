import os

def Exists(Arch):
        try:
            arch = open(Arch, "rt")
            arch.close()

        except FileNotFoundError or FileExistsError:
            return False
            
        else:
            return True
            arch.close()


def CreateArchive(Arch):
    try:
        arch = open(Arch, "wt+")
        arch.close()

    except:
        print("ERRO AO CRIAR O ARQUIVO!")

    finally:
         arch.close


def register(Name, Age, Archive):
    try:
        local_archive = open(Archive, "at")
    except:
        print("[ERRO] Houve um erro ao abrir o arquivo de cadastros")
    
    else:
        try:
            local_archive.write(f"{Name};{Age}\n")

        except:
             print("[ERRO] Houve um erro ao registrar o cadastro no arquivo de cadastros")

        else:
             print("Cadastro realizado com SUCESSO!")


    finally:
        local_archive.close()