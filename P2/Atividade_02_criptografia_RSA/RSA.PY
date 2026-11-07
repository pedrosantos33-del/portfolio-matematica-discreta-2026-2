
def eh_primo(numero):
    if numero < 2:
        return False

    divisor = 2

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1

    return True


def calcular_mdc(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def calcular_inverso(a, n):
    r1 = a
    r2 = n
    x1 = 1
    x2 = 0

    while r2 != 0:
        quociente = r1 // r2

        r1, r2 = r2, r1 - quociente * r2
        x1, x2 = x2, x1 - quociente * x2

    if r1 != 1:
        return None

    return x1 % n


def potencia_modular(base, expoente, modulo):
    resultado = 1
    base = base % modulo

    print("\n--- Etapas da Exponenciacao Modular ---")

    while expoente > 0:
        print(f"Expoente atual: {expoente}")
        print(f"Resultado atual: {resultado}")
        print(f"Base atual: {base}")

        if expoente % 2 == 1:
            resultado = (resultado * base) % modulo
            print(f"Multiplicacao: resultado = {resultado}")

        base = (base * base) % modulo
        expoente = expoente // 2

        print("------------------------------")

    return resultado


# ==========================================
# PARTE A - PRIMALIDADE E PARAMETROS RSA
# ==========================================

print("========== PARTE A ==========")

p = int(input("Digite o numero primo p: "))
q = int(input("Digite o numero primo q: "))

while p <= 1 or q <= 1 or p == q or not eh_primo(p) or not eh_primo(q):
    print("Erro! p e q devem ser primos, distintos e maiores que 1.")

    p = int(input("Digite novamente p: "))
    q = int(input("Digite novamente q: "))

n = p * q
phi = (p - 1) * (q - 1)

print("\n--- Parametros RSA ---")
print(f"p = {p}")
print(f"q = {q}")
print(f"n = {p} * {q} = {n}")
print(f"phi(n) = {phi}")


# ==========================================
# PARTE B - CONSTRUCAO DAS CHAVES
# ==========================================

print("\n========== PARTE B ==========")

e = int(input("Digite o expoente publico e: "))

while e <= 1 or e >= phi or calcular_mdc(e, phi) != 1:
    print("Erro! e deve ser maior que 1, menor que phi(n) e coprimo com phi(n).")
    e = int(input("Digite novamente o expoente publico e: "))

d = calcular_inverso(e, phi)

print("\n--- Chaves RSA ---")
print(f"MDC({e}, {phi}) = {calcular_mdc(e, phi)}")
print(f"Expoente privado d = {d}")
print(f"Verificacao: ({e} * {d}) % {phi} = {(e * d) % phi}")
print(f"Chave publica: ({e}, {n})")
print(f"Chave privada: ({d}, {n})")


# ==========================================
# PARTE C - CIFRAGEM E DECIFRAGEM
# ==========================================

print("\n========== PARTE C ==========")

M = int(input(f"Digite a mensagem inteira M (0 ate {n - 1}): "))

while M < 0 or M >= n:
    print(f"Erro! M deve estar entre 0 e {n - 1}.")
    M = int(input("Digite novamente a mensagem M: "))

print("\n--- Cifragem ---")

C = potencia_modular(M, e, n)

print(f"\nMensagem original: {M}")
print(f"Numero cifrado: {C}")

print("\n--- Decifragem ---")

M_recuperado = potencia_modular(C, d, n)

print(f"\nMensagem original: {M}")
print(f"Numero cifrado: {C}")
print(f"Mensagem decifrada: {M_recuperado}")

if M_recuperado == M:
    print("Sucesso! A mensagem original foi recuperada.")
else:
    print("Erro! A mensagem recuperada e diferente da original.")


# ==========================================
# PARTE D - TEOREMAS DE EULER E FERMAT
# ==========================================

print("\n========== PARTE D ==========")

# Teorema de Euler

print("\n--- Teorema de Euler ---")

mdc = calcular_mdc(M, n)

print(f"MDC({M}, {n}) = {mdc}")

if mdc == 1:
    print("A base e o modulo sao coprimos.")
    print(f"phi(n) = {phi}")

    resultado_euler = potencia_modular(M, phi, n)

    print(f"\n{M}^{phi} mod {n} = {resultado_euler}")

    if resultado_euler == 1:
        print("Teorema de Euler confirmado!")
    else:
        print("Resultado inesperado.")
else:
    print("Nao e possivel aplicar diretamente o Teorema de Euler.")
    print("A base nao e coprima com o modulo.")
    print("Utilize a exponenciacao modular por reducoes sucessivas.")


# Pequeno Teorema de Fermat

print("\n--- Pequeno Teorema de Fermat ---")

a = int(input("Digite uma base a para o teste de Fermat: "))

while a % p == 0:
    print(f"Erro! A base nao pode ser divisivel por {p}.")
    a = int(input("Digite outra base a: "))

resultado_fermat = potencia_modular(a, p - 1, p)

print(f"\nModulo primo p = {p}")
print(f"Base escolhida a = {a}")
print(f"{a}^{p - 1} mod {p} = {resultado_fermat}")

if resultado_fermat == 1:
    print("Pequeno Teorema de Fermat confirmado!")
else:
    print("Resultado inesperado.")
