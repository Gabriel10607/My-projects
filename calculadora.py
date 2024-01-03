conta = int(
    input(
        """Escolha uma equação:
[ 1 ] Soma
[ 2 ] Subtração
[ 3 ] Multiplicação
[ 4 ] Divisão
minha escolha:"""
    )
)
if conta == 1:
    n1 = float(input("DIgite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    soma = n1 + n2
    print("A soma entre {} e {} é igual a {}".format(n1, n2, soma))
elif conta == 2:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número:"))
    subtração = n1 - n2
    print("A subtração entre {} e {} é igual a {}".format(n1, n2, subtração))
elif conta == 3:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    multiplicação = n1 * n2
    print("O produto de {} por {} é igual a {}".format(n1, n2, multiplicação))
elif conta == 4:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    divisão = n1 / n2
    print("O quociente entre {} e {} é igual a {}".format(n1, n2, divisão))
else:
    print("opção inválida!!!")
