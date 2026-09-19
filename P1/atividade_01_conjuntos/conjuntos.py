print("================================")
print("PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA")
print("Disciplina: Estruturas Matemáticas para Computação")
print("Atividade 1 - Teoria dos Conjuntos")
print("Nome: Pedro Henrique Vieira dos Santos")
print("Matrícula: 2622130002")
print("Disciplina: Estruturas Matemáticas para Computação")
print("Turno: Matutino")
print("================================")

A = set(input("Digite os elementos do conjunto A: ").split()) 
B = set(input("Digite os elementos do conjunto B: ").split())

uniao = A | B
print("A ∪ B =", uniao)

intersecçao = A & B
print("A ∩ B =", intersecçao)

diferençaAB = A - B
print("A - B =", diferençaAB)

diferençaBA = B - A
print("B - A =", diferençaBA)

cardinalidadeA = len(A)
cardinalidadeB = len(B)
cardinalidade_uniao = len(A | B)
cardinalidade_intersecçao = len(A & B)
print("Cardinalidade de A:", cardinalidadeA)
print("Cardinalidade de B:", cardinalidadeB)
print("Cardinalidade de A ∪ B:", cardinalidade_uniao)
print("Cardinalidade de A ∩ B:", cardinalidade_intersecçao)

def gerar_partes(conjunto):
    partes = {frozenset()}

    for elemento in conjunto:
        nova_partes = set()
        for subset in partes:
            nova_partes.add(subset | {elemento})
        partes |= nova_partes

    return partes


partesA = gerar_partes(A)
partesB = gerar_partes(B)

print("Conjunto das partes de A:", partesA)
print("Conjunto das partes de B:", partesB)

cardinalidade_partesA = len(partesA)
cardinalidade_partesB = len(partesB)

print("Cardinalidade do conjunto das partes de A:", cardinalidade_partesA)
print("Cardinalidade do conjunto das partes de B:", cardinalidade_partesB)


elementosA = list(A)

particaoA = []

for i, elemento in enumerate(elementosA):
    if i % 2 == 0:
        particaoA.append(set())

    particaoA[-1].add(elemento)

print("Exemplo de partição de A:", particaoA)

produto_cartesiano = {(a, b) for a in A for b in B}

print("A × B =", produto_cartesiano)

print("A está contido em B?", A <= B)
print("B está contido em A?", B <= A)