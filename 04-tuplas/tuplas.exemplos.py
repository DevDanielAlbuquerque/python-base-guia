# =============================================================
# TUPLAS EM PYTHON — Do básico ao avançado
# Tuplas são coleções ORDENADAS e IMUTÁVEIS.
# Use quando os dados não devem ser alterados após a criação.
# =============================================================

# -------------------------------------------------------------
# EXEMPLO 1 — Criação e acesso básico
# Diferente da lista, usa parênteses () em vez de colchetes [].
# Suporta indexação e fatiamento da mesma forma que listas.
# -------------------------------------------------------------

cidade = ("Rio de Janeiro", -22.9, -43.1)

print(cidade[0])     # Rio de Janeiro  — acesso por índice
print(cidade[1:])    # (-22.9, -43.1)  — fatiamento

# Tupla é IMUTÁVEL — tentar alterar gera TypeError
# cidade[0] = "São Paulo"   # ← descomente para ver o erro


# -------------------------------------------------------------
# EXEMPLO 2 — Tupla com um único elemento e tipo
# Uma tupla de 1 elemento precisa da vírgula final.
# -------------------------------------------------------------

unico = (42,)       # é uma tupla
nao_tupla = (42)    # é apenas um int entre parênteses

print(type(unico))      # <class 'tuple'>
print(type(nao_tupla))  # <class 'int'>

# Verificar se é tupla
print(isinstance(cidade, tuple))   # True
print(len(cidade))                 # 3 elementos


# -------------------------------------------------------------
# EXEMPLO 3 — Desempacotamento (unpacking)
# Distribui os valores da tupla em variáveis de forma elegante.
# O operador * captura múltiplos valores restantes.
# -------------------------------------------------------------

ponto = (10, 20, 30)

x, y, z = ponto          # desempacotamento total
print(f"x={x}, y={y}, z={z}")

# Desempacotamento parcial com *
primeiro, *meio, ultimo = (1, 2, 3, 4, 5)
print(primeiro)   # 1
print(meio)       # [2, 3, 4]
print(ultimo)     # 5

# Troca de variáveis com tupla (sem variável auxiliar!)
a, b = 10, 20
a, b = b, a       # internamente Python cria uma tupla temporária
print(a, b)       # 20 10


# -------------------------------------------------------------
# EXEMPLO 4 — namedtuple: tupla com campos nomeados
# Melhora a legibilidade ao nomear cada posição da tupla.
# Importada do módulo collections.
# -------------------------------------------------------------

from collections import namedtuple

# Define o "molde" da namedtuple
Ponto = namedtuple("Ponto", ["x", "y"])
Pessoa = namedtuple("Pessoa", ["nome", "idade", "cidade"])

p = Ponto(3, 7)
print(p.x, p.y)       # 3 7  — acesso por nome, não por índice

daniel = Pessoa("Daniel", 25, "SP")
print(daniel.nome)    # Daniel
print(daniel)         # Pessoa(nome='Daniel', idade=25, cidade='SP')


# -------------------------------------------------------------
# EXEMPLO 5 — Tuplas como chaves de dicionário e retorno múltiplo — AVANÇADO
# Por serem imutáveis, tuplas podem ser chaves de dicionário (listas não).
# Funções usam tuplas implicitamente para retornar múltiplos valores.
# -------------------------------------------------------------

# Tupla como chave de dicionário (coordenadas → nome do local)
mapa = {
    (-22.9, -43.1): "Rio de Janeiro",
    (-23.5, -46.6): "São Paulo",
    (-15.7, -47.9): "Brasília",
}

coordenada = (-23.5, -46.6)
print(mapa[coordenada])   # São Paulo

# Função com retorno múltiplo (retorna uma tupla implicitamente)
def estatisticas(numeros):
    """Retorna mínimo, máximo e média de uma lista."""
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

dados = [4, 8, 15, 16, 23, 42]
minimo, maximo, media = estatisticas(dados)
print(f"Min: {minimo} | Max: {maximo} | Média: {media:.1f}")
