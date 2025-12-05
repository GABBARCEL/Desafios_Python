import os

def Exists(Arch):
        try:
            arch = open(Arch, "rt")
            arch.close()

        except FileNotFoundError or FileExistsError:
              return False
        
        else:
              return True
        

def CreateArchive(Arch):
    try:
        arch = open(Arch, "wt+")
        arch.close()

    except:
        print("ERRO AO CRIAR O ARQUIVO!")