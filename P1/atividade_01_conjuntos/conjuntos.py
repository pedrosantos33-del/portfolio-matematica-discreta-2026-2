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
