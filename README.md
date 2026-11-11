# 📘 Python — guia de fundamentos

Repositório de estudos e consulta com exemplos comentados de Python. Reúne fundamentos da linguagem e alguns recursos complementares, como comprehensions, namedtuple e decoradores.

Meu objetivo é consolidar a programação para aplicar esses conhecimentos em scripts, automações e integrações nos estudos de sistemas e nuvem.

## Requisitos

- **Python 3.10 ou superior**, necessário para o exemplo de `match/case`.
- Os nove módulos principais usam apenas a biblioteca padrão do Python; não exigem instalação de pacotes com pip.

## Conteúdo

| Módulo | Conteúdo |
| --- | --- |
| [01 — Condicionais](01-condicionais/exemplos.py) | if, elif, else, expressão condicional e match/case |
| [02 — Laços](02-lacos/exemplos.py) | for, while, break, continue, range e enumerate |
| [03 — Listas](03-listas/exemplos.py) | Métodos, fatiamento, comprehensions e zip |
| [04 — Tuplas](04-tuplas/exemplos.py) | Imutabilidade, desempacotamento, namedtuple e retorno múltiplo |
| [05 — Conjuntos](05-conjuntos-set/exemplos.py) | Unicidade, operações de conjuntos e comprehensions |
| [06 — Dicionários](06-dicionarios/exemplos.py) | Chaves e valores, métodos, estruturas aninhadas e defaultdict |
| [07 — Strings](07-strings/exemplos.py) | Métodos, formatação e manipulação de texto |
| [08 — Funções](08-funcoes/exemplos.py) | Parâmetros, retorno, args, kwargs, lambda, closures e decoradores |
| [09 — SQLite](09-sqlite/exemplos.py) | Conexão, criação de tabela, inserção, consulta e atualização |

A ordem é uma sugestão de leitura. Os exemplos complementares não representam uma trilha completa de Python avançado.

## Como executar

Clone o repositório e entre na pasta:

```bash
git clone https://github.com/DevDanielAlbuquerque/python-base-guia.git
cd python-base-guia
```

Execute um módulo a partir da raiz:

```bash
python 01-condicionais/exemplos.py
python 03-listas/exemplos.py
```

Use `python3` ou `py` se esse for o comando configurado no seu ambiente. Confira a versão com `python --version`.

### Exemplo interativo de laços

```bash
python 02-lacos/exemplos.py
```

O script solicita uma senha fictícia: `wordfish`. Digite esse valor para continuar os exemplos. Esse trecho demonstra um laço while, sem implementar autenticação real.

### Exemplo SQLite

```bash
python 09-sqlite/exemplos.py
```

O script cria `meu_banco.db` no diretório de execução e demonstra operações com dados de exemplo. O DELETE está comentado. Ao executar novamente, o INSERT OR REPLACE substitui o registro de mesma chave antes da atualização.

## Como uso este material

1. Ler o exemplo e prever o resultado.
2. Executar e comparar a saída com os comentários.
3. Alterar valores e condições para observar o comportamento.
4. Tentar escrever uma solução semelhante sem copiar.

Este repositório é um guia de consulta e prática; a aplicação desses fundamentos também será registrada em projetos próprios.

## Referência separada

A pasta [referencias/azure-functions](referencias/azure-functions/README.md) preserva um exemplo antigo de Azure Functions, SQL Server e Telegram que estava misturado ao módulo SQLite. Ele está fora dos módulos principais, requer serviços e dependências externas e não foi validado como aplicação funcional nesta revisão.

## Verificação

Na revisão de 11/11/2026, os nove módulos principais foram executados em ambiente temporário. O módulo de laços recebeu a entrada esperada e o SQLite utilizou um banco temporário. Isso verifica a execução dos exemplos, sem cobrir todos os cenários ou representar testes completos.

## Autor

Daniel Albuquerque — estudos em programação, sistemas, automação e nuvem.
