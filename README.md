==============================================
PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA
==============================================

Aluno: Pedro Henrique Vieira dos Santos

Matrícula: 2622130002

Disciplina: Estruturas Matemáticas para Computação

Turno: Matutino

================================================


Atividade 1 – Congruência Modular e Teorema Chinês do Resto

Parte A – Verificação de Congruência Modular

Arquivo:

P1/Atividade_01_congruencia_e_teorema_chines/congruencia.py

Como executar:

Execute o arquivo congruencia.py pelo terminal utilizando Python.

O programa solicitará três números inteiros: a, b e n, sendo n obrigatoriamente maior que zero.

Exemplo de entrada:

Digite o valor de a: 23
Digite o valor de b: 8
Digite o valor de n: 5

================================================

O programa apresenta:

Diferença entre os valores de a e b;

Resto da divisão da diferença por n;

Verificação se o resto é igual a zero;

Conclusão informando se a e b são congruentes módulo n;

Justificativa matemática do resultado.

Exemplo de resultado:

--- Verificação de Congruência ---
Diferença entre a e b: 23 - 8 = 15
Resto da divisão de 15 por 5: 0
23 e 8 são congruentes módulo 5.
Justificativa: a diferença é divisível por n.

================================================

Parte B – Teorema Chinês do Resto

Arquivo:

P1/atividade_01_congruencia_e_teorema_chines/teorema_chines.py

Como executar:

Execute o arquivo teorema_chines.py pelo terminal utilizando Python.

O programa solicitará a quantidade de congruências (3 ou 4) e, em seguida, os restos e módulos correspondentes de cada equação.

Os módulos devem ser positivos e dois a dois coprimos.

Exemplo de entrada:


Quantidade de congruências (3 ou 4): 3

Congruência 1:
Digite o resto: 2
Digite o módulo: 3

Congruência 2:
Digite o resto: 3
Digite o módulo: 5

Congruência 3:
Digite o resto: 2
Digite o módulo: 7

================================================

O programa apresenta:

Verificação se os módulos são positivos e dois a dois coprimos;

Produto dos módulos (N);

Cálculo dos valores Ni para cada congruência;

Cálculo dos inversos multiplicativos pelo Algoritmo de Euclides Estendido;

Cálculo das parcelas utilizadas na fórmula do Teorema Chinês do Resto;

Soma das parcelas e solução reduzida módulo N;

Solução geral do sistema (x = x0 + t · N);

Verificação da solução em todas as congruências.

================================================

Exemplo de resultado:

Produto dos módulos: N = 105

Soma das parcelas: 233
Solução reduzida: x0 = 23
Módulo total: N = 105
Solução geral: x = 23 + 105t,
t pertencente aos inteiros

A solução encontrada satisfaz as três congruências do sistema.



================================================



Atividade 2 – Criptografia RSA

Partes A, B, C e D – Primalidade, Construção das Chaves, Cifragem, Decifragem e Teoremas de Euler e Fermat


Arquivo:

P1/atividade_02_criptografia_RSA/RSA.py

Como executar:

Execute o arquivo RSA.py pelo terminal utilizando Python.

O programa solicitará dois números inteiros distintos e maiores que 1 (p e q), verificando se ambos são primos. Em seguida, calculará os parâmetros RSA: o módulo n e a função totiente de Euler φ(n).

Depois, solicitará o expoente público e, verificando se ele é válido e coprimo com φ(n). Com esses valores, calculará o expoente privado d por meio do algoritmo de Euclides estendido, apresentando as chaves pública e privada.

Na sequência, solicitará uma mensagem inteira M, respeitando a condição 0 ≤ M < n. O programa realizará a cifragem utilizando a chave pública e a decifragem utilizando a chave privada, apresentando as etapas da exponenciação modular e verificando se a mensagem original foi recuperada.

Por fim, demonstrará a aplicação do Teorema de Euler, verificando a condição de coprimalidade entre a base e o módulo RSA, e do Pequeno Teorema de Fermat, utilizando o módulo primo p e uma base a que não seja divisível por ele.

================================================

Exemplo de entrada:

p = 5

q = 11

e = 3

M = 7

a = 2 (base para o teste de Fermat)

O programa apresenta:

Verificação de primalidade dos números p e q.

Validação de que p e q são distintos e maiores que 1.

Cálculo do módulo RSA: n = p × q.

Cálculo da função totiente: φ(n) = (p - 1) × (q - 1).

Validação do expoente público e.

Cálculo do máximo divisor comum entre e e φ(n).

Cálculo do expoente privado d pelo algoritmo de Euclides estendido.

Verificação da relação e × d ≡ 1 (mod φ(n)).

Apresentação da chave pública (e, n) e da chave privada (d, n).

Validação da mensagem original, garantindo que 0 ≤ M < n.

Cifragem da mensagem por meio da exponenciação modular: C ≡ Mᵉ (mod n).

Apresentação das etapas da exponenciação modular.

Decifragem utilizando a chave privada: M' ≡ Cᵈ (mod n).

Comparação entre a mensagem original e a mensagem recuperada.

Implementação da exponenciação modular por reduções sucessivas, evitando a construção de potências inteiras muito grandes.

Verificação da condição de coprimalidade para aplicação do Teorema de Euler.

Demonstração do Teorema de Euler: M^φ(n) ≡ 1 (mod n), quando M e n são coprimos.

Verificação das condições de aplicação do Pequeno Teorema de Fermat.

Demonstração do Pequeno Teorema de Fermat: a^(p-1) ≡ 1 (mod p), utilizando um módulo primo e uma base não divisível por ele.

================================================

Exemplo de resultado:

Para os valores informados:

p = 5 e q = 11

n = 55

φ(n) = 40

e = 3

d = 27

Chave pública: (3, 55)

Chave privada: (27, 55)

Cifragem:

C ≡ 7³ (mod 55)

C = 13

Decifragem:

M' ≡ 13²⁷ (mod 55)

M' = 7

Verificação da mensagem:

Como M' = M, a mensagem original foi recuperada corretamente.

Teorema de Euler:

MDC(7, 55) = 1

7⁴⁰ mod 55 = 1

Teorema de Euler confirmado.

Pequeno Teorema de Fermat:

Para a = 2 e p = 5:

2⁴ mod 5 = 1

Pequeno Teorema de Fermat confirmado.






