from random import randint

computador = randint(1, 20)
print("Estou a pensar num número entre 1 e 20. Tens 3 tentativas para acertar.")
num = int(input("Adivinha: "))
if num > computador:
    num1 = int(input("Tenta um número menor: "))

    if num1 > computador:
        num2 = int(input("Tenta um número menor: "))
        if num2 == computador:
            print("MUITOS PARABÉNS!!! Acertaste no número que eu estava a pensar.")
        else:
            print(
                """Você ERROU, o número que eu estava a pensar era {}.
                  TENTE NOVAMENTE.""".format(
                    computador
                )
            )
    elif num1 < computador:
        num3 = int(input("Tenta um número maior: "))
        if num3 == computador:
            print("MUITOS PARABÉNS!!! Acertaste no número que eu estava a pensar.")
        else:
            print(
                """Você ERROU, o número que eu estava a pensar era {}.
                  TENTE NOVAMENTE.""".format(
                    computador
                )
            )
    else:
        print("MUITOS PARABÉNS!!! Acertaste no número que eu estava a pensar.")

elif num < computador:
    num4 = int(input("Tenta um número maior: "))
    if num4 > computador:
        num5 = int(input("Tenta um número menor: "))
        if num5 == computador:
            print("MUITOS PARABÉNS!!! Acertaste no número que eu estava a pensar.")
        else:
            print(
                """Você ERROU. O número que eu estava a pensar era {}.
                  TENTE NOVAMENTE""".format(
                    computador
                )
            )
    elif num4 < computador:
        num6 = int(input("Tenta um número maior: "))
        if num6 == computador:
            print("MUITOS PARABÉNS!!! Acertaste no número que eu estava a pensar.")
        else:
            print(
                """Você ERROU. O número que eu estava a pensar era {}.
                  TENTE NOVAMENTE.""".format(
                    computador
                )
            )
    else:
        print("MUITOS PARABÉNS!!! Acertaste no número que eu estava a pensar.")

else:
    print("MUITOS PARABÉNS!!! Acertaste no número que eu estava a pensar.")
