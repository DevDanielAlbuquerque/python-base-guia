# =============================================================
# CONJUNTOS (SET) EM PYTHON — Exemplos comentados
# Sets são coleções NÃO ORDENADAS, SEM DUPLICATAS e MUTÁVEIS.
# Ideais para eliminar repetições e realizar operações matemáticas de conjunto.
# =============================================================

# -------------------------------------------------------------
# EXEMPLO 1 — Criação e propriedades básicas
# Sets removem automaticamente valores duplicados.
# Não possuem índice — não é possível acessar por posição.
# -------------------------------------------------------------

numeros = {1, 2, 2, 3, 4, 4, 4}
print(numeros)   # {1, 2, 3, 4} — duplicatas foram removidas

# Criando set a partir de uma lista (forma comum para remover duplicatas)
lista_com_repeticoes = ["python", "java", "python", "c", "java"]
linguagens = set(lista_com_repeticoes)
print(linguagens)   # ex: {'java', 'c', 'python'} — ordem pode variar

# Verificar pertencimento (O(1) em média; pior caso O(n))
print("python" in linguagens)   # True
print("ruby" in linguagens)     # False


# -------------------------------------------------------------
# EXEMPLO 2 — Operações matemáticas de conjunto
# union        → todos os elementos de A e B (A ∪ B)
# intersection → apenas os elementos presentes em ambos (A ∩ B)
# difference   → elementos de A que não estão em B (A − B)
# -------------------------------------------------------------

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))           # {1, 2, 3, 4, 5, 6}
print(A | B)                # mesma coisa com operador |

print(A.intersection(B))    # {3, 4}
print(A & B)                # mesma coisa com operador &

print(A.difference(B))      # {1, 2}  — está em A mas não em B
print(A - B)                # mesma coisa com operador -


# -------------------------------------------------------------
# EXEMPLO 3 — Métodos para modificar sets
# add    → adiciona um único elemento
# remove → remove (lança KeyError se não existir)
# discard→ remove sem erro se não existir
# clear  → esvazia o set
# -------------------------------------------------------------

cores = {"vermelho", "azul", "verde"}

cores.add("amarelo")         # adiciona "amarelo"
cores.discard("roxo")        # não faz nada se não existir (seguro)
cores.remove("azul")         # remove "azul" (KeyError se não existir)

print(cores)   # {'vermelho', 'verde', 'amarelo'} (ordem pode variar)

# Tamanho e conversão
print(len(cores))         # 3
print(list(cores))        # converte para lista (se precisar de ordenação)


# -------------------------------------------------------------
# EXEMPLO 4 — symmetric_difference, issubset e issuperset
# symmetric_difference → elementos que estão em A ou B, mas não em ambos (A △ B)
# issubset   → verifica se todos os elementos de A estão em B
# issuperset → verifica se B contém todos os elementos de A
# -------------------------------------------------------------

X = {1, 2, 3}
Y = {2, 3, 4, 5}

print(X.symmetric_difference(Y))   # {1, 4, 5}
print(X ^ Y)                       # mesmo resultado com operador ^

# Subconjunto e superconjunto
vogais = {"a", "e", "i", "o", "u"}
subset = {"a", "e"}

print(subset.issubset(vogais))     # True  — subset ⊆ vogais
print(vogais.issuperset(subset))   # True  — vogais ⊇ subset
print(subset.isdisjoint({"x"}))    # True  — nenhum elemento em comum


# -------------------------------------------------------------
# EXEMPLO 5 — Set comprehension e caso de uso prático — AVANÇADO
# Similar à list comprehension, mas gera um set (sem duplicatas).
# Muito útil para análise e filtragem de dados.
# -------------------------------------------------------------

# Set comprehension: quadrados perfeitos de 1 a 10
quadrados = {n ** 2 for n in range(1, 11)}
print(quadrados)   # {1, 4, 9, 16, 25, 36, 49, 64, 81, 100}

# Caso de uso: encontrar palavras únicas em um texto
texto = "o rato roeu a roupa do rei de roma e o rei ficou sem roupa"
palavras_unicas = {palavra for palavra in texto.split()}
print(palavras_unicas)
print(f"Total de palavras únicas: {len(palavras_unicas)}")

# Encontrar alunos que estão na turma A E na turma B (interseção)
turma_a = {"Ana", "Bruno", "Carlos", "Diana"}
turma_b = {"Bruno", "Diana", "Eduardo", "Flávia"}

em_ambas = turma_a & turma_b
so_em_a  = turma_a - turma_b

print(f"Em ambas as turmas: {em_ambas}")   # {'Bruno', 'Diana'}
print(f"Apenas na turma A: {so_em_a}")     # {'Ana', 'Carlos'}
