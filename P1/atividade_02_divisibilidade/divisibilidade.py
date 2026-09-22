print("================================")
print("PORTFOLIO DE PROGRAMACAO MATEMATICA")
print("Disciplina: Estruturas Matematicas para Computacao")
print("Atividade 2 - Divisibilidade")
print("Nome: Pedro Henrique Vieira dos Santos")
print("Matricula: 2622130002")
print("Turno: Matutino")
print("================================")

# O código abaixo solicita ao usuário que digite dois números inteiros A e B. int(input()) é usado para converter a entrada do usuário em um número inteiro.
A= int(input("Digite um numero inteiro A: "))
B= int(input("Digite um numero inteiro B: "))

#operações de divisibilidade
div = A // B
mod = A % B

#guarda os valores originais de A e B para calcular o mdc e mmc posteriormente
A_original = A
B_original = B

# O loop while continua enquanto B não for igual a 0. Dentro do loop, ele calcula o resto da divisão de A por B (mod) e imprime o resultado. Em seguida, atualiza os valores de A e B para continuar o processo de cálculo do mdc usando o algoritmo de Euclides.
while B != 0:
    mod = A % B
    print(A, "mod", B, "=", mod)
    A = B
    B = mod

#calcula o mmc usando a relação entre mdc e mmc: mmc(A, B) = (A * B) / mdc(A, B). Aqui, A é o mdc calculado no loop while.
mmc = (A_original * B_original) // A

print("div = ", div)
print("mod = ", mod)
print("mdc = ", A)
print("mmc = ", mmc)