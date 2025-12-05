def Title(Entry = "Defaut Text"):
    print("=" * 42)
    print(Entry.center(42))
    print("=" * 42)


def Menu(Menu_list = ["Test 1", "Test 2"]):
    c = 1
    for i in range(0, len(Menu_list)):
        print(f"{c}* {Menu_list[i]}")
        c += 1


def Page(Page):
    print("=" * 42)
    print(f"Página da opção {Page}")


def Exit():
    print("=" * 42)
    print("Saindo...".center(42))
    print("=" * 42)


def Input(var_list, exit_option):
    while True:
        try:
            Local_Value = int(input("Sua opção: "))
        
        except:
            print("[ERRO], valor não aceitável")
            continue
        
        else:
            if Local_Value not in range(1, len(var_list) + 1):
                print("[ERRO], opção não existênte")
                continue

            elif Local_Value == exit_option:
                Exit()
                break

            else:
                Page(Local_Value)
                continue