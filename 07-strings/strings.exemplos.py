# =============================================================
# STRINGS EM PYTHON — Do básico ao avançado
# Strings são sequências IMUTÁVEIS de caracteres.
# Python oferece dezenas de métodos nativos para manipulá-las.
# =============================================================

# -------------------------------------------------------------
# EXEMPLO 1 — Métodos básicos de transformação
# upper / lower / title / strip / replace
# -------------------------------------------------------------

curso = "pYtHon"

print(curso.upper())    # PYTHON   — tudo maiúsculo
print(curso.lower())    # python   — tudo minúsculo
print(curso.title())    # Python   — primeira letra de cada palavra maiúscula

# strip remove espaços (ou caracteres) das extremidades
email = "  usuario@email.com  "
print(email.strip())    # 'usuario@email.com'

# replace substitui todas as ocorrências
frase = "Eu amo Java. Java é ótimo."
print(frase.replace("Java", "Python"))
# Eu amo Python. Python é ótimo.


# -------------------------------------------------------------
# EXEMPLO 2 — Formatação de strings
# f-string (Python 3.6+) é a forma mais moderna e legível.
# format() é a forma clássica e mais compatível.
# % é a forma antiga (evitar em código novo).
# -------------------------------------------------------------

nome = "Daniel"
idade = 25
altura = 1.75

# f-string: expressões dentro de {}
print(f"Olá, {nome}! Você tem {idade} anos.")

# Formatar números: casas decimais, largura, zero à esquerda
print(f"Altura: {altura:.2f} m")       # 1.75
print(f"Nota: {9.5:05.2f}")            # 09.50 — 5 chars, 2 decimais
print(f"Hex: {255:#x}")                # 0xff

# .format() — útil quando f-string não está disponível
print("Nome: {0}, Idade: {1}".format(nome, idade))
print("Pi ≈ {valor:.4f}".format(valor=3.14159))


# -------------------------------------------------------------
# EXEMPLO 3 — Indexação e fatiamento
# Strings funcionam como sequências — suportam índice e slice.
# -------------------------------------------------------------

texto = "Python é incrível"

# Acesso por índice (base 0)
print(texto[0])     # P
print(texto[-1])    # l  — último caractere

# Fatiamento [início:fim:passo]
print(texto[:6])    # Python   — primeiros 6 caracteres
print(texto[9:])    # incrível — do índice 9 ao final
print(texto[::2])   # Pto  nc íe — de 2 em 2
print(texto[::-1])  # révírcni é nohtyP — invertida

# Verificar conteúdo
print("Python" in texto)        # True
print(texto.startswith("Py"))   # True
print(texto.endswith("vel"))    # True


# -------------------------------------------------------------
# EXEMPLO 4 — split(), join() e outras ferramentas
# split  → divide a string em uma lista
# join   → une uma lista em string
# find   → retorna índice da primeira ocorrência (-1 se não achar)
# count  → conta ocorrências de uma substring
# -------------------------------------------------------------

frase = "maçã,banana,laranja,uva"

# split: divide pela vírgula
frutas = frase.split(",")
print(frutas)   # ['maçã', 'banana', 'laranja', 'uva']

# join: une a lista com " | " como separador
print(" | ".join(frutas))   # maçã | banana | laranja | uva

# find e count
texto = "banana é uma fruta. banana é amarela."
print(texto.find("banana"))    # 0   — índice da primeira ocorrência
print(texto.count("banana"))   # 2   — quantas vezes aparece

# Dividir linha de CSV em campos
linha_csv = "Daniel,25,SP,Python"
campos = linha_csv.split(",")
print(campos[0], campos[3])   # Daniel Python


# -------------------------------------------------------------
# EXEMPLO 5 — Métodos avançados e expressões regulares — AVANÇADO
# zfill, ljust, rjust para alinhamento e padding.
# maketrans + translate para substituição de múltiplos caracteres.
# re (regex) para padrões complexos de busca/substituição.
# -------------------------------------------------------------

import re

# Padding e alinhamento
codigo = "42"
print(codigo.zfill(6))          # 000042 — preenche com zeros à esq
print("ok".ljust(10, "-"))      # ok--------
print("ok".rjust(10, "-"))      # --------ok
print("ok".center(10, "*"))     # ****ok****

# maketrans + translate: substituição de tabela de caracteres
tabela = str.maketrans("aeiou", "AEIOU")   # mapeia minúsculas → maiúsculas
print("python é fantástico".translate(tabela))
# pythOn É fAntástIcO (só as vogais ficam maiúsculas)

# Expressões regulares com re
texto = "Contato: (11) 98765-4321 ou (21) 3344-5566"

# Encontrar todos os números de telefone
telefones = re.findall(r"\(\d{2}\)\s?\d{4,5}-\d{4}", texto)
print(telefones)   # ['(11) 98765-4321', '(21) 3344-5566']

# Validar formato de e-mail
email = "usuario@dominio.com.br"
padrao = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
valido = bool(re.match(padrao, email))
print(f"E-mail válido: {valido}")   # True
