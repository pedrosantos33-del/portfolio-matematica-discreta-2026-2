print("================================")
print("PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA")
print("Disciplina: Estruturas Matemáticas para Computação")
print("Atividade 1 - Teoria dos Conjuntos")
print("Nome: Pedro Henrique Vieira dos Santos")
print("Matrícula: 2622130002")
print("Disciplina: Estruturas Matemáticas para Computação")
print("Turno: Matutino")
print("================================")

# set é a variavel que representa o conjunto A, input() é a função que recebe a entrada do usuário, split() divide a string em uma lista de elementos separados por espaço e set() converte a lista em um conjunto.
A = set(input("Digite os elementos do conjunto A: ").split()) 
B = set(input("Digite os elementos do conjunto B: ").split())

# Operações de conjuntos
uniao = A | B
print("A ∪ B =", uniao)

intersecçao = A & B
print("A ∩ B =", intersecçao)

diferençaAB = A - B
print("A - B =", diferençaAB)

diferençaBA = B - A
print("B - A =", diferençaBA)

#len() é a função que retorna o número de elementos de um conjunto.
cardinalidadeA = len(A)
cardinalidadeB = len(B)
cardinalidade_uniao = len(A | B)
cardinalidade_intersecçao = len(A & B)
print("Cardinalidade de A:", cardinalidadeA)
print("Cardinalidade de B:", cardinalidadeB)
print("Cardinalidade de A ∪ B:", cardinalidade_uniao)
print("Cardinalidade de A ∩ B:", cardinalidade_intersecçao)

#def gerar_partes(conjunto) é a função que gera o conjunto das partes de um conjunto dado. O conjunto das partes é o conjunto de todos os subconjuntos possíveis de um conjunto, incluindo o conjunto vazio e o próprio conjunto.
def gerar_partes(conjunto):
    # frozenset() representa o conjunto vazio de forma imutável.
# Ele é usado porque um set comum não pode ser colocado dentro de outro set.
# Assim, {frozenset()} representa um conjunto que contém o conjunto vazio.
    partes = {frozenset()}

#for elemento in conjunto: é um loop que percorre cada elemento do conjunto dado. Para cada elemento, ele cria novos subconjuntos adicionando o elemento atual a cada subconjunto existente no conjunto das partes.
#nova_partes = set() cria um novo conjunto vazio para armazenar os novos subconjuntos gerados ao adicionar o elemento atual.
#for subset in partes: percorre cada subconjunto existente no conjunto das partes. Para cada subconjunto, ele cria um novo subconjunto que é a união do subconjunto atual com o elemento atual.
#nova_partes.add(subset | {elemento}) adiciona o novo subconjunto gerado ao conjunto nova_partes.
#partes |= nova_partes atualiza o conjunto das partes com os novos subconjuntos gerados, garantindo que todos os subconjuntos possíveis sejam incluídos.
    for elemento in conjunto:
        nova_partes = set()
        for subset in partes:
            nova_partes.add(subset | {elemento})
        partes |= nova_partes

#return partes finaliza a função retornando o conjunto das partes gerado.
    return partes

def mostrar_partes(partes):
    # Ordena pelo tamanho do subconjunto
    partes_ordenadas = sorted(
        partes,
        key=lambda subset: (len(subset), sorted(subset))
    )

    for subset in partes_ordenadas:
        if not subset:
            print("∅")
        else:
            elementos = ", ".join(sorted(subset))
            print("{" + elementos + "}")

# Gerar o conjunto das partes de A e B usando a função gerar_partes
partesA = gerar_partes(A)
partesB = gerar_partes(B)

print("Conjunto das partes de A:" )
mostrar_partes(partesA)
print("Conjunto das partes de B:" )
mostrar_partes(partesB)

cardinalidade_partesA = len(partesA)
cardinalidade_partesB = len(partesB)

print("Cardinalidade do conjunto das partes de A:", cardinalidade_partesA)
print("Cardinalidade do conjunto das partes de B:", cardinalidade_partesB)

# organizar os elementos de A em uma lista para poder particionar
elementosA = list(A)

particaoA = []

# Divide os elementos de A em grupos de até 2 elementos.
# Os grupos formados são subconjuntos disjuntos cuja união corresponde ao conjunto A, formando uma partição de A.
for i, elemento in enumerate(elementosA):
    if i % 2 == 0:
        particaoA.append(set())

    particaoA[-1].add(elemento)

print("Exemplo de partição de A:", particaoA)

#para cada elemento em A, ele cria um par ordenado (a, b) para cada elemento em B usando uma compreensão de conjunto. O resultado é o produto cartesiano de A e B, que é armazenado na variável produto_cartesiano.
produto_cartesiano = {(a, b) for a in A for b in B}

print("A × B =", produto_cartesiano)

print("A está contido em B?", A <= B)
print("B está contido em A?", B <= A)