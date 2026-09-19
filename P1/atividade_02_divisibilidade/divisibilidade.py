print("================================")
print("PORTFOLIO DE PROGRAMACAO MATEMATICA")
print("Disciplina: Estruturas Matematicas para Computacao")
print("Atividade 2 - Divisibilidade")
print("Nome: Pedro Henrique Vieira dos Santos")
print("Matricula: 2622130002")
print("Turno: Matutino")
print("================================")

A= int(input("Digite um numero inteiro A: "))
B= int(input("Digite um numero inteiro B: "))

div = A // B
mod = A % B

A_original = A
B_original = B

while B != 0:
    mod = A % B
    print(A, "mod", B, "=", mod)
    A = B
    B = mod

mmc = (A_original * B_original) // A

print("div = ", div)
print("mod = ", mod)
print("mdc = ", A)
print("mmc = ", mmc)