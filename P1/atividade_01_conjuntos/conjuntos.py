A = set(input("Digite os elementos do conjunto A: ").split())
B = set(input("Digite os elementos do conjunto B: ").split())

uniao = A | B
print(uniao)

interseccao = A & B
print(interseccao)

diferençaAB = A - B
print(diferençaAB) 

diferençaBA = B - A
print(diferençaBA)

cardinalidadeA = 