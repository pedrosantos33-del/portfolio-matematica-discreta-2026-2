
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
n = int(input("Digite o valor de n: "))

while n <= 0:
    print("Erro! O valor de n deve ser maior que zero.")
    n = int(input("Digite novamente o valor de n: "))

diferenca = a - b
resto = diferenca % n

print("\n--- Verificação de Congruência ---")
print(f"Diferença entre a e b: {a} - {b} = {diferenca}")
print(f"Resto da divisão de {diferenca} por {n}: {resto}")

if resto == 0:
    print(f"{a} e {b} são congruentes módulo {n}.")
    print("Justificativa: a diferença é divisível por n.")
else:
    print(f"{a} e {b} não são congruentes módulo {n}.")
    print("Justificativa: a diferença não é divisível por n.")
