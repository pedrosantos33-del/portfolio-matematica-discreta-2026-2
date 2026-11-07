
def eh_primo(numero):
    print(f"\n--- Verificacao de primalidade de {numero} ---")

    if numero < 2:
        print(f"{numero} nao e primo, pois e menor que 2.")
        return False

    divisor = 2

    while divisor * divisor <= numero:
        resto = numero % divisor

        print(f"{numero} % {divisor} = {resto}")

        if resto == 0:
            print(f"{numero} e divisivel por {divisor}.")
            print("Portanto, nao e primo.")
            return False

        divisor += 1

    print(f"{numero} e primo.")
    return True


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
    print(f"\n--- Calculo do inverso de {a} modulo {n} ---")

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


def potencia_modular(base, expoente, modulo):
    print("\n--- Etapas da Exponenciacao Modular ---")

    resultado = 1
    base = base % modulo

    print(f"Base inicial reduzida: {base}")
    print(f"Expoente inicial: {expoente}")
    print(f"Modulo: {modulo}")

    while expoente > 0:
        print(f"\nExpoente atual: {expoente}")
        print(f"Resultado atual: {resultado}")
        print(f"Base atual: {base}")

        if expoente % 2 == 1:
            resultado = (resultado * base) % modulo
            print(f"Expoente impar: resultado = ({resultado})")

        base = (base * base) % modulo
        expoente = expoente // 2

        print(f"Nova base: {base}")
        print(f"Novo expoente: {expoente}")
        print("------------------------------")

    print(f"Resultado final da exponenciacao modular: {resultado}")

    return resultado


print("======================================")
print("       CRIPTOGRAFIA RSA")
print("======================================")


# PARTE A - Geracao das chaves

print("\n--- PARTE A: GERACAO DAS CHAVES ---")

p = int(input("Digite o primeiro numero primo (p): "))
q = int(input("Digite o segundo numero primo (q): "))

while p <= 1 or q <= 1 or p == q or not eh_primo(p) or not eh_primo(q):
    print("\nErro! Digite dois numeros primos distintos e maiores que 1.")

    p = int(input("Digite novamente o primeiro numero primo (p): "))
    q = int(input("Digite novamente o segundo numero primo (q): "))

n = p * q
phi = (p - 1) * (q - 1)

print("\n--- Calculo dos parametros RSA ---")
print(f"n = p * q = {p} * {q} = {n}")
print(f"phi(n) = (p - 1) * (q - 1)")
print(f"phi(n) = ({p} - 1) * ({q} - 1) = {phi}")


# PARTE B - Calculo da chave privada

print("\n--- PARTE B: CALCULO DA CHAVE PRIVADA ---")

e = int(input("Digite o expoente publico (e): "))

mdc = calcular_mdc(e, phi)

while e <= 1 or e >= phi or mdc != 1:
    print("\nErro! O valor de e deve ser maior que 1,")
    print("menor que phi(n) e coprimo com phi(n).")

    e = int(input("Digite novamente o expoente publico (e): "))
    mdc = calcular_mdc(e, phi)

d = calcular_inverso(e, phi)

print("\n--- Chaves RSA ---")
print(f"Chave publica: ({e}, {n})")
print(f"Chave privada: ({d}, {n})")

print(f"\nVerificacao: ({e} * {d}) % {phi} = {(e * d) % phi}")


# PARTE C - Criptografia e descriptografia

print("\n--- PARTE C: CRIPTOGRAFIA E DESCRIPTOGRAFIA ---")

M = int(input(f"Digite a mensagem numerica (0 ate {n - 1}): "))

while M < 0 or M >= n:
    print(f"Erro! A mensagem deve estar entre 0 e {n - 1}.")
    M = int(input("Digite novamente a mensagem: "))

print("\n--- Criptografando a mensagem ---")
print(f"Formula: C = M^e mod n")
print(f"C = {M}^{e} mod {n}")

C = potencia_modular(M, e, n)

print("\n--- Descriptografando a mensagem ---")
print(f"Formula: M' = C^d mod n")
print(f"M' = {C}^{d} mod {n}")

M_recuperado = potencia_modular(C, d, n)

print("\n--- Resultado da criptografia ---")
print(f"Mensagem original: {M}")
print(f"Mensagem criptografada: {C}")
print(f"Mensagem recuperada: {M_recuperado}")

if M == M_recuperado:
    print("Verificacao concluida: a mensagem foi recuperada corretamente.")
else:
    print("Erro: a mensagem recuperada e diferente da original.")


# PARTE D - Exponenciacao modular e teoremas

print("\n--- PARTE D: EXPONENCIACAO MODULAR E TEOREMAS ---")


# Teorema de Euler

print("\n--- Aplicacao do Teorema de Euler ---")

mdc_euler = calcular_mdc(M, n)

if mdc_euler == 1:
    print(f"\nComo MDC({M}, {n}) = 1,")
    print("as condicoes do Teorema de Euler foram satisfeitas.")

    print(f"Aplicando: {M}^{phi} mod {n}")

    resultado_euler = potencia_modular(M, phi, n)

    print("\n--- Resultado do Teorema de Euler ---")
    print(f"{M}^{phi} mod {n} = {resultado_euler}")

    if resultado_euler == 1:
        print("A igualdade do Teorema de Euler foi confirmada.")
    else:
        print("A igualdade esperada nao foi confirmada.")

else:
    print(f"\nMDC({M}, {n}) = {mdc_euler}.")
    print("A mensagem e o modulo nao sao coprimos.")
    print("Portanto, nao podemos aplicar diretamente o Teorema de Euler.")
    print("A exponenciacao modular continua sendo valida.")


# Pequeno Teorema de Fermat

print("\n--- Aplicacao do Pequeno Teorema de Fermat ---")

print(f"O numero primo utilizado sera p = {p}.")

a = int(input("Digite a base (a) para o Teorema de Fermat: "))

while a % p == 0:
    print(f"Erro! A base nao pode ser divisivel por {p}.")
    a = int(input("Digite novamente a base (a): "))

print(f"\nVerificacao: {a} % {p} = {a % p}")
print("A base nao e divisivel pelo numero primo.")

print("\nAplicando o Pequeno Teorema de Fermat:")
print(f"{a}^{p - 1} mod {p}")

resultado_fermat = potencia_modular(a, p - 1, p)

print("\n--- Resultado do Pequeno Teorema de Fermat ---")
print(f"{a}^{p - 1} mod {p} = {resultado_fermat}")

if resultado_fermat == 1:
    print("A igualdade do Pequeno Teorema de Fermat foi confirmada.")
else:
    print("A igualdade esperada nao foi confirmada.")

print("\n======================================")
print("       FIM DO PROGRAMA RSA")
print("======================================")
