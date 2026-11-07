
def calcular_mdc(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a


def calcular_inverso(a, n):
    mdc = calcular_mdc(a, n)

    if mdc != 1:
        return None

    r1 = a
    r2 = n
    x1 = 1
    x2 = 0

    while r2 != 0:
        quociente = r1 // r2

        r1, r2 = r2, r1 - quociente * r2
        x1, x2 = x2, x1 - quociente * x2

    return x1 % n


print("--- Teorema Chinês do Resto ---")

quantidade = int(input("Quantidade de congruências (3 ou 4): "))

while quantidade != 3 and quantidade != 4:
    print("Erro! Escolha 3 ou 4 congruências.")
    quantidade = int(input("Quantidade de congruências (3 ou 4): "))

restos = []
modulos = []

for i in range(quantidade):
    print(f"\nCongruência {i + 1}:")
    a = int(input("Digite o resto: "))
    n = int(input("Digite o módulo: "))

    restos.append(a)
    modulos.append(n)

validos = True

for i in range(quantidade):
    if modulos[i] <= 0:
        validos = False

for i in range(quantidade):
    for j in range(i + 1, quantidade):
        if modulos[i] > 0 and modulos[j] > 0:
            if calcular_mdc(modulos[i], modulos[j]) != 1:
                validos = False

if not validos:
    print("\nSistema fora das condições previstas para esta atividade.")

else:
    N = 1

    for n in modulos:
        N = N * n

    print("\n--- Cálculos do Teorema Chinês do Resto ---")
    print(f"Produto dos módulos: N = {N}")

    soma = 0

    for i in range(quantidade):
        Ni = N // modulos[i]
        inverso = calcular_inverso(Ni, modulos[i])

        parcela = restos[i] * Ni * inverso
        soma = soma + parcela

        print(f"\nCongruência {i + 1}:")
        print(f"N{i + 1} = {N} / {modulos[i]} = {Ni}")
        print(f"Inverso de {Ni} módulo {modulos[i]} = {inverso}")
        print(f"Parcela = {restos[i]} * {Ni} * {inverso} = {parcela}")

    x0 = soma % N

    print("\n--- Resultado ---")
    print(f"Soma das parcelas: {soma}")
    print(f"Solução reduzida: x0 = {x0}")
    print(f"Módulo total: N = {N}")
    print(f"Solução geral: x = {x0} + {N}t, t pertencente aos inteiros")

    print("\n--- Verificação das congruências ---")

    for i in range(quantidade):
        resultado = x0 % modulos[i]

        print(
            f"{x0} % {modulos[i]} = {resultado} "
            f"(resto esperado: {restos[i] % modulos[i]})"
        )

        if resultado == restos[i] % modulos[i]:
            print("Congruência satisfeita.")
        else:
            print("Erro na verificação da congruência.")
