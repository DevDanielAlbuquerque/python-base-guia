# =============================================================
# DICIONÁRIOS EM PYTHON — Exemplos comentados
# Dicionários armazenam pares chave → valor.
# São MUTÁVEIS, ORDENADOS (Python 3.7+) e as chaves são ÚNICAS.
# =============================================================

# -------------------------------------------------------------
# EXEMPLO 1 — Criação e acesso básico
# Acesse valores pela chave usando [] ou .get()
# .get() é mais seguro pois retorna None (ou padrão) se não existir.
# -------------------------------------------------------------

pessoa = {"nome": "Daniel", "idade": 25, "cidade": "SP"}

print(pessoa["nome"])                  # Daniel
print(pessoa.get("telefone"))          # None  — chave inexistente sem erro
print(pessoa.get("telefone", "N/A"))   # N/A   — valor padrão

# Adicionando e atualizando chaves
pessoa["telefone"] = "9999-0000"       # adiciona nova chave
pessoa["idade"] = 26                   # atualiza valor existente
print(pessoa)


# -------------------------------------------------------------
# EXEMPLO 2 — Métodos úteis: update, pop, keys, values, items
# update  → atualiza/mescla com outro dicionário
# pop     → remove e retorna o valor pela chave
# keys    → retorna todas as chaves
# values  → retorna todos os valores
# items   → retorna pares (chave, valor)
# -------------------------------------------------------------

produto = {"nome": "Notebook", "preco": 3500.00, "estoque": 10}

produto.update({"preco": 3200.00, "marca": "Dell"})  # atualiza e adiciona
removido = produto.pop("estoque")   # remove e retorna 10

print(list(produto.keys()))     # ['nome', 'preco', 'marca']
print(list(produto.values()))   # ['Notebook', 3200.0, 'Dell']
print(removido)                 # 10


# -------------------------------------------------------------
# EXEMPLO 3 — Iterando sobre um dicionário
# for chave, valor in dicionario.items() é o idioma mais comum.
# -------------------------------------------------------------

notas = {"Ana": 9.5, "Bruno": 7.0, "Carlos": 8.8}

# Iterando sobre chaves e valores ao mesmo tempo
for aluno, nota in notas.items():
    status = "Aprovado" if nota >= 7 else "Reprovado"
    print(f"{aluno}: {nota:.1f} → {status}")

print("---")

# Verificar se chave existe antes de acessar
if "Ana" in notas:
    print(f"Nota da Ana: {notas['Ana']}")


# -------------------------------------------------------------
# EXEMPLO 4 — Dict comprehension
# Cria dicionários de forma concisa a partir de iterações.
# Sintaxe: {chave: valor for item in iterável if condição}
# -------------------------------------------------------------

# Quadrado de cada número como valor
quadrados = {n: n ** 2 for n in range(1, 6)}
print(quadrados)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filtrar apenas aprovados
notas = {"Ana": 9.5, "Bruno": 5.0, "Carlos": 7.8, "Diana": 4.5}
aprovados = {aluno: nota for aluno, nota in notas.items() if nota >= 6}
print(aprovados)   # {'Ana': 9.5, 'Carlos': 7.8}

# Inverter chave e valor (útil para lookup reverso)
siglas = {"SP": "São Paulo", "RJ": "Rio de Janeiro", "MG": "Minas Gerais"}
invertido = {v: k for k, v in siglas.items()}
print(invertido["São Paulo"])   # SP


# -------------------------------------------------------------
# EXEMPLO 5 — Dicionários aninhados e defaultdict — AVANÇADO
# Dicionários podem ter outros dicionários como valores.
# defaultdict cria automaticamente chaves com valor padrão.
# -------------------------------------------------------------

from collections import defaultdict

# Dicionário aninhado: dados de funcionários
empresa = {
    "E001": {"nome": "Alice",  "cargo": "Dev",     "salario": 8000},
    "E002": {"nome": "Bruno",  "cargo": "Designer", "salario": 6000},
    "E003": {"nome": "Carla",  "cargo": "Dev",     "salario": 9000},
}

# Acesso em dicionário aninhado
print(empresa["E001"]["nome"])          # Alice
print(empresa["E003"]["salario"])       # 9000

# Agrupar funcionários por cargo
for codigo, dados in empresa.items():
    print(f"[{codigo}] {dados['nome']} — {dados['cargo']}")

print("---")

# defaultdict: agrupa itens sem precisar verificar se chave existe
grupos = defaultdict(list)   # ao acessar chave nova, cria uma lista vazia

for codigo, dados in empresa.items():
    grupos[dados["cargo"]].append(dados["nome"])

print(dict(grupos))
# {'Dev': ['Alice', 'Carla'], 'Designer': ['Bruno']}