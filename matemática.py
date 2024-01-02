import math  # importa a biblioteca para as operações matemáticas necessárias #

r = float(input("Indica o valor do raio: "))  # vai pedir o valor do raio #
if r <= 0:  # se o raio for menor ou igual a 0 vai responder que o problema não tem solução #
    print("O problema não tem solução.")
else:  # para todo o raio não seja igual ou menor a 0 vai indicar a respetiva área #
    h = r * math.sin(math.radians(60))
    AT = (h * r) / 2
    AC = math.pi * r**2
    As = AC / 6
    A1 = (AC / 2 - 2 * AT - As) / 2
    RA = 2 * As - 4 * A1
    print(
        "A área da região azul é aproximadamente igual a {} u.a.".format(round(RA, 2))
    )
