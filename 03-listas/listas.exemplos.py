# =============================================================
# LISTAS EM PYTHON — Do básico ao avançado
# Listas são coleções ORDENADAS e MUTÁVEIS que aceitam qualquer tipo.
# =============================================================

# -------------------------------------------------------------
# EXEMPLO 1 — Criação e acesso básico
# Índices começam em 0. Índices negativos contam do final.
# -------------------------------------------------------------

tarefas = ["Estudar", "Treinar", "Dormir"]

print(tarefas[0])    # Estudar   — primeiro elemento
print(tarefas[-1])   # Dormir    — último elemento
print(len(tarefas))  # 3         — tamanho da lista


# -------------------------------------------------------------
# EXEMPLO 2 — Métodos para modificar listas
# append → adiciona ao final
# insert → adiciona em posição específica
# remove → remove pelo valor
# pop    → remove pelo índice (e retorna o valor)
# sort   → ordena a lista in-place
# -------------------------------------------------------------

frutas = ["banana", "maçã", "uva"]

frutas.append("laranja")         # adiciona ao final
frutas.insert(1, "abacaxi")      # insere na posição 1
frutas.remove("uva")             # remove pelo valor
removida = frutas.pop(0)         # remove e retorna "banana"
frutas.sort()                    # ordena em ordem alfabética

print(frutas)      # ['abacaxi', 'laranja', 'maçã']
print(removida)    # banana


# -------------------------------------------------------------
# EXEMPLO 3 — Fatiamento (slicing)
# Sintaxe: lista[início:fim:passo]  — o fim é exclusivo
# -------------------------------------------------------------

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numeros[2:6])     # [2, 3, 4, 5]   — do índice 2 ao 5
print(numeros[:4])      # [0, 1, 2, 3]   — do início ao 3
print(numeros[7:])      # [7, 8, 9]      — do 7 ao final
print(numeros[::2])     # [0, 2, 4, 6, 8] — de 2 em 2
print(numeros[::-1])    # [9, 8, ..., 0]  — lista invertida


# -------------------------------------------------------------
# EXEMPLO 4 — List comprehension
# Forma concisa de criar listas a partir de iterações/filtros.
# Sintaxe: [expressão for item in iterável if condição]
# -------------------------------------------------------------

# Forma tradicional com for:
quadrados_for = []
for n in range(1, 6):
    quadrados_for.append(n ** 2)

# Forma compacta com comprehension:
quadrados = [n ** 2 for n in range(1, 6)]
print(quadrados)     # [1, 4, 9, 16, 25]

# Filtro com condição:
pares = [n for n in range(20) if n % 2 == 0]
print(pares)         # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Transformação de strings:
nomes = ["alice", "bob", "carlos"]
maiusculos = [nome.upper() for nome in nomes]
print(maiusculos)    # ['ALICE', 'BOB', 'CARLOS']


# -------------------------------------------------------------
# EXEMPLO 5 — Listas aninhadas (matrizes) e zip() — AVANÇADO
# Listas podem conter outras listas, formando estruturas 2D.
# zip() combina duas listas elemento a elemento.
# -------------------------------------------------------------

# Matriz 3x3 (lista de listas)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Acessando elemento da linha 1, coluna 2 (índice base 0)
print(matriz[1][2])   # 6

# Percorrendo todos os elementos com loops aninhados
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()   # quebra de linha ao final de cada linha da matriz

# zip: emparelha elementos de duas listas
alunos = ["Ana", "Bruno", "Carla"]
notas  = [9.5, 7.0, 8.8]

for aluno, nota in zip(alunos, notas):
    status = "Aprovado" if nota >= 7 else "Reprovado"
    print(f"{aluno}: {nota} → {status}")
