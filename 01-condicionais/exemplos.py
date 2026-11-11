# =============================================================
# CONDICIONAIS EM PYTHON — Exemplos comentados
# =============================================================

# -------------------------------------------------------------
# EXEMPLO 1 — if / else básico
# Verifica uma única condição e executa um bloco ou outro.
# -------------------------------------------------------------

idade = 20

if idade >= 18:
    print("Entrada permitida")   # executado quando a condição é verdadeira
else:
    print("Entrada negada")      # executado quando a condição é falsa


# -------------------------------------------------------------
# EXEMPLO 2 — if / elif / else (múltiplas condições)
# Usa elif para testar várias possibilidades em sequência.
# O primeiro bloco verdadeiro é executado e os demais ignorados.
# -------------------------------------------------------------

nome = "Latam"

if nome == "Alura":
    print("Bem-vindo à Alura!")
elif nome == "Latam":
    print("Bem-vindo à Latam!")   # este bloco é ativado
else:
    print("Nome desconhecido")


# -------------------------------------------------------------
# EXEMPLO 3 — Condicionais aninhadas (if dentro de if)
# Útil quando precisamos verificar condições dentro de condições.
# -------------------------------------------------------------

usuario_logado = True
perfil = "admin"

if usuario_logado:
    if perfil == "admin":
        print("Painel administrativo liberado")
    else:
        print("Painel de usuário comum")
else:
    print("Faça login para continuar")


# -------------------------------------------------------------
# EXEMPLO 4 — Operador ternário (expressão condicional inline)
# Escreve um if/else em uma única linha de forma concisa.
# Sintaxe: valor_se_verdadeiro if condição else valor_se_falso
# -------------------------------------------------------------

pontos = 75
resultado = "Aprovado" if pontos >= 60 else "Reprovado"
print(resultado)  # Aprovado

# Outro uso: atribuir um valor padrão
desconto = 0.1 if pontos > 70 else 0.0
print(f"Desconto aplicado: {desconto * 100:.0f}%")  # 10%


# -------------------------------------------------------------
# EXEMPLO 5 — match / case (Python 3.10+) — AVANÇADO
# Substitui longas cadeias de if/elif de forma mais legível.
# Funciona como o "switch" de outras linguagens, mas mais poderoso.
# -------------------------------------------------------------

comando = "sair"

match comando:
    case "iniciar":
        print("Sistema iniciando...")
    case "pausar":
        print("Sistema pausado.")
    case "sair":
        print("Encerrando sistema.")  # este bloco é ativado
    case _:
        # O underscore (_) é o caso padrão (equivalente ao else)
        print("Comando desconhecido.")

# match também funciona com valores numéricos e estruturas complexas
codigo_http = 404

match codigo_http:
    case 200:
        print("OK — Requisição bem-sucedida")
    case 404:
        print("Not Found — Recurso não encontrado")  # ativado
    case 500:
        print("Server Error — Erro interno do servidor")
    case _:
        print(f"Código {codigo_http} não mapeado")
