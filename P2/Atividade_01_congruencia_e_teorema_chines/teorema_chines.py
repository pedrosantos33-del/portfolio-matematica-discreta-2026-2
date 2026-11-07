


def calcular_mdc(a, b):
    print(f"\n--- Calculo do MDC({a}, {b}) ---")

    valor_a = a
    valor_b = b

    while b != 0:
        quociente = a // b
        resto = a % b

        print(f"{a} = {b} * {quociente} + {resto}")

        a, b = b, resto

    print(f"MDC({valor_a}, {valor_b}) = {a}")

    return a


def calcular_inverso(a, n):
    print(f"\n--- Inverso multiplicativo de {a} modulo {n} ---")

    r1 = a
    r2 = n
    x1 = 1
    x2 = 0

    while r2 != 0:
        quociente = r1 // r2

        novo_r = r1 - quociente * r2
        novo_x = x1 - quociente * x2

        print(f"{r1} = {quociente} * {r2} + {novo_r}")
        print(f"Coeficiente atualizado: {novo_x}")

        r1, r2 = r2, novo_r
        x1, x2 = x2, novo_x

    if r1 != 1:
        print("Nao existe inverso multiplicativo.")
        return None

    inverso = x1 % n

    print(f"Inverso encontrado: {inverso}")
    print(f"Verificacao: ({a} * {inverso}) % {n} = {(a * inverso) % n}")

    return inverso


print("--- Teorema Chines do Resto ---")

quantidade = int(input("Quantidade de congruencias (3 ou 4): "))

while quantidade != 3 and quantidade != 4:
    print("Erro! Escolha 3 ou 4 congruencias.")
    quantidade = int(input("Quantidade de congruencias (3 ou 4): "))

restos = []
modulos = []

for i in range(quantidade):
    print(f"\nCongruencia {i + 1}:")
    a = int(input("Digite o resto: "))
    n = int(input("Digite o modulo: "))

    restos.append(a)
    modulos.append(n)


# Verificacao das condicoes dos modulos

validos = True

print("\n--- Verificacao dos modulos ---")

for i in range(quantidade):
    if modulos[i] <= 0:
        print(f"Modulo {modulos[i]} invalido. O modulo deve ser positivo.")
        validos = False

if validos:
    print("\n--- Verificacao da coprimalidade ---")

    for i in range(quantidade):
        for j in range(i + 1, quantidade):

            mdc = calcular_mdc(modulos[i], modulos[j])

            if mdc == 1:
                print(f"Os modulos {modulos[i]} e {modulos[j]} sao coprimos.")
            else:
                print(f"Os modulos {modulos[i]} e {modulos[j]} NAO sao coprimos.")
                validos = False


if not validos:
    print("\nSistema fora das condicoes previstas para esta atividade.")

else:

    # Calculo do produto dos modulos

    N = 1

    print("\n--- Produto dos modulos ---")

    for n in modulos:
        print(f"N = {N} * {n} = {N * n}")
        N = N * n

    print(f"Produto final dos modulos: N = {N}")


    # Aplicacao do Teorema Chines do Resto

    print("\n--- Calculos do Teorema Chines do Resto ---")

    soma = 0

    for i in range(quantidade):

        Ni = N // modulos[i]

        inverso = calcular_inverso(Ni, modulos[i])

        parcela = restos[i] * Ni * inverso
        soma = soma + parcela

        print(f"\nCongruencia {i + 1}:")
        print(f"N{i + 1} = {N} / {modulos[i]} = {Ni}")
        print(f"Inverso de {Ni} modulo {modulos[i]} = {inverso}")
        print(f"Parcela = {restos[i]} * {Ni} * {inverso} = {parcela}")


    # Calculo da solucao final

    x0 = soma % N

    print("\n--- Resultado ---")
    print(f"Soma das parcelas: {soma}")
    print(f"Como x0 e o resto da divisao de {soma} por {N}:")
    print(f"x0 = {soma} % {N} = {x0}")
    print(f"Modulo total: N = {N}")
    print(f"Solucao geral: x = {x0} + {N}t, t pertencente aos inteiros")


    # Verificacao das congruencias

    print("\n--- Verificacao das congruencias ---")

    for i in range(quantidade):

        resultado = x0 % modulos[i]

        print(
            f"{x0} % {modulos[i]} = {resultado} "
            f"(resto esperado: {restos[i] % modulos[i]})"
        )

        if resultado == restos[i] % modulos[i]:
            print("Congruencia satisfeita.")
        else:
            print("Erro na verificacao da congruencia.")

