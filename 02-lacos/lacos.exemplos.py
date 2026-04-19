# =============================================================
# LAÇOS (LOOPS) EM PYTHON — Do básico ao avançado
# =============================================================

# -------------------------------------------------------------
# EXEMPLO 1 — for básico iterando sobre uma lista
# O for percorre cada item de uma sequência automaticamente.
# -------------------------------------------------------------

nomes = ["Carlos", "Ana", "Pedro"]

for nome in nomes:
    print(nome)  # imprime cada nome da lista na sequência


# -------------------------------------------------------------
# EXEMPLO 2 — while: repete enquanto a condição for verdadeira
# Use quando não sabe antecipadamente quantas repetições serão feitas.
# -------------------------------------------------------------

contador = 0

while contador < 5:
    print("Contador:", contador)
    contador += 1   # IMPORTANTE: sempre atualizar a variável para evitar loop infinito

# Exemplo prático: sistema de senha com while
senha = "wordfish"
master = input("Digite a senha: ")

while master != senha:
    print("Senha errada!")
    master = input("Tente novamente: ")

print("Acesso liberado! ✅")


# -------------------------------------------------------------
# EXEMPLO 3 — break e continue: controlando o fluxo do loop
# break  → interrompe o loop imediatamente
# continue → pula para a próxima iteração sem executar o restante
# -------------------------------------------------------------

# break: para o loop quando n chega em 5
for n in range(10):
    if n == 5:
        break        # sai do loop, números 5-9 nunca são impressos
    print(n)

print("---")

# continue: pula os números ímpares, imprime apenas os pares
for n in range(10):
    if n % 2 != 0:
        continue     # vai direto para a próxima iteração
    print(n)


# -------------------------------------------------------------
# EXEMPLO 4 — for com range() e enumerate()
# range() gera sequências numéricas
# enumerate() fornece índice + valor ao mesmo tempo
# -------------------------------------------------------------

# range(início, fim, passo) — o fim é exclusivo
print("Contagem regressiva:")
for i in range(10, 0, -1):   # de 10 até 1, passo -1
    print(i, end=" ")
print("Lançar! 🚀")

print("---")

# enumerate: útil para ter o índice sem usar range(len(...))
frutas = ["maçã", "banana", "laranja"]
for indice, fruta in enumerate(frutas, start=1):
    print(f"{indice}. {fruta}")  # 1. maçã, 2. banana, 3. laranja


# -------------------------------------------------------------
# EXEMPLO 5 — Loops aninhados + cláusula else — AVANÇADO
# Loops podem ser aninhados (loop dentro de loop).
# A cláusula else em loops é executada quando o loop termina
# normalmente (sem break).
# -------------------------------------------------------------

# Loops aninhados: tabuada de multiplicação (3x3)
print("\nTabuada 1 a 3:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")

# else no for: verifica se um número é primo
print("\nNúmeros primos de 2 a 20:")
for num in range(2, 21):
    for divisor in range(2, num):
        if num % divisor == 0:
            break          # encontrou divisor, não é primo
    else:
        # O else só executa se o for terminou SEM break
        print(num, end=" ")   # 2 3 5 7 11 13 17 19