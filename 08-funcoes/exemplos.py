# =============================================================
# FUNÇÕES EM PYTHON — Exemplos comentados
# Funções são blocos reutilizáveis de código definidos com def.
# Permitem organizar, abstrair e reutilizar lógica.
# =============================================================

# -------------------------------------------------------------
# EXEMPLO 1 — Função básica com parâmetros e retorno
# def define a função, return devolve o resultado.
# Sem return, a função retorna None implicitamente.
# -------------------------------------------------------------

def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def exibir_mensagem(nome):
    """Exibe uma saudação. Não tem return (retorna None)."""
    print(f"Olá, {nome}!")

resultado = somar(10, 5)
print(resultado)          # 15

exibir_mensagem("Daniel")  # Olá, Daniel!


# -------------------------------------------------------------
# EXEMPLO 2 — Parâmetros padrão (default) e keyword arguments
# Parâmetros com valor padrão se tornam opcionais na chamada.
# Keyword arguments permitem chamar em qualquer ordem pelo nome.
# -------------------------------------------------------------

def criar_perfil(nome, idade, cidade="Desconhecida", ativo=True):
    """Cria e retorna um dicionário de perfil."""
    return {
        "nome": nome,
        "idade": idade,
        "cidade": cidade,
        "ativo": ativo,
    }

p1 = criar_perfil("Alice", 30)                          # usa defaults
p2 = criar_perfil("Bruno", 25, cidade="SP", ativo=False) # sobrescreve
p3 = criar_perfil(idade=28, nome="Carla", cidade="RJ")   # keyword args

print(p1)
print(p2)
print(p3)


# -------------------------------------------------------------
# EXEMPLO 3 — *args e **kwargs: número variável de argumentos
# *args   → captura argumentos posicionais extras como tupla
# **kwargs→ captura argumentos nomeados extras como dicionário
# -------------------------------------------------------------

def exibir_poema(*args):
    """Aceita qualquer número de linhas."""
    for linha in args:
        print(linha)

exibir_poema(
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
)

print("---")

def registrar_evento(tipo, **kwargs):
    """Registra um evento com campos dinâmicos."""
    print(f"[{tipo.upper()}]")
    for chave, valor in kwargs.items():
        print(f"  {chave}: {valor}")

registrar_evento("login", usuario="daniel", ip="192.168.1.1", porta=443)


# -------------------------------------------------------------
# EXEMPLO 4 — Funções lambda (anônimas) e funções de alta ordem
# lambda cria funções pequenas sem nome em uma única linha.
# map(), filter() e sorted() aceitam funções como argumento.
# -------------------------------------------------------------

# Lambda básica
dobrar = lambda x: x * 2
print(dobrar(7))   # 14

# sorted com key: ordena por critério personalizado
alunos = [
    {"nome": "Carlos", "nota": 7.5},
    {"nome": "Ana",    "nota": 9.0},
    {"nome": "Bruno",  "nota": 6.0},
]
por_nota = sorted(alunos, key=lambda a: a["nota"], reverse=True)
for a in por_nota:
    print(f"{a['nome']}: {a['nota']}")

# map: aplica função a cada elemento
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda n: n ** 2, numeros))
print(quadrados)   # [1, 4, 9, 16, 25]

# filter: mantém apenas os elementos que satisfazem a condição
pares = list(filter(lambda n: n % 2 == 0, numeros))
print(pares)       # [2, 4]


# -------------------------------------------------------------
# EXEMPLO 5 — Closures e decoradores — AVANÇADO
# Closure: função interna que "lembra" do escopo externo.
# Decorator: função que envolve outra para adicionar comportamento.
# -------------------------------------------------------------

# Closure: fábrica de multiplicadores
def criar_multiplicador(fator):
    """Retorna uma função que multiplica pelo fator capturado."""
    def multiplicar(numero):
        return numero * fator   # "lembra" do fator do escopo externo
    return multiplicar

dobrar  = criar_multiplicador(2)
triplicar = criar_multiplicador(3)

print(dobrar(5))     # 10
print(triplicar(5))  # 15

# Decorator: adiciona log automático a qualquer função
def log_chamada(func):
    """Decorator que exibe nome da função e seus argumentos."""
    def wrapper(*args, **kwargs):
        print(f"→ Chamando '{func.__name__}' com args={args}, kwargs={kwargs}")
        resultado = func(*args, **kwargs)
        print(f"← Retornou: {resultado}")
        return resultado
    return wrapper

@log_chamada   # equivale a: calcular_imc = log_chamada(calcular_imc)
def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal."""
    return round(peso / altura ** 2, 2)

imc = calcular_imc(70, 1.75)
print(f"IMC: {imc}")
