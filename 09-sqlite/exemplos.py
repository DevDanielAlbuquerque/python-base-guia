import sqlite3


# =============================================================
# SQLITE EM PYTHON — VERSAO SIMPLES PARA INICIANTE
# Neste arquivo voce vai ver os comandos mais comuns:
# 1) conectar no banco
# 2) criar tabela
# 3) inserir dados
# 4) consultar dados
# 5) atualizar dados
# 6) deletar dados
# =============================================================


# Nome do arquivo do banco de dados.
# Se ele nao existir, o SQLite cria automaticamente.
nome_banco = "meu_banco.db"
conexao = None
cursor = None


# Bloco principal do programa.
# Tudo comeca aqui quando executamos este arquivo diretamente.
if __name__ == "__main__":
    try:
        # -----------------------------------------------------
        # 1) CONEXAO COM O BANCO
        # connect abre a conexao com o arquivo .db.
        # cursor e o objeto que executa os comandos SQL.
        # -----------------------------------------------------
        conexao = sqlite3.connect(nome_banco)
        cursor = conexao.cursor()

        # -----------------------------------------------------
        # 2) CREATE TABLE
        # Cria a tabela Pessoa caso ela ainda nao exista.
        # cpf sera a chave primaria, ou seja, valor unico.
        # -----------------------------------------------------
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Pessoa (
                cpf INTEGER NOT NULL,
                nome TEXT NOT NULL,
                nascimento TEXT NOT NULL,
                oculos BOOLEAN NOT NULL,
                PRIMARY KEY (cpf)
            );
            """
        )

        # Salva a criacao da tabela no arquivo do banco.
        conexao.commit()

        # -----------------------------------------------------
        # 3) INSERT
        # Insere uma pessoa no banco.
        # Usamos parametros nomeados para evitar montar SQL com
        # concatenacao de string.
        # -----------------------------------------------------
        pessoa = {
            "cpf": 20000000099,
            "nome": "Jose",
            "nascimento": "1990-02-28",
            "oculos": False,
        }

        cursor.execute(
            """
            INSERT OR REPLACE INTO Pessoa (cpf, nome, nascimento, oculos)
            VALUES (:cpf, :nome, :nascimento, :oculos);
            """,
            pessoa,
        )

        # Salva o registro inserido.
        conexao.commit()

        # -----------------------------------------------------
        # 4) SELECT
        # Busca todos os registros da tabela Pessoa.
        # fetchall devolve uma lista com todas as linhas encontradas.
        # -----------------------------------------------------
        cursor.execute(
            """
            SELECT cpf, nome, nascimento, oculos
            FROM Pessoa
            ORDER BY nome;
            """
        )

        pessoas = cursor.fetchall()

        print("\nPessoas cadastradas:")
        for cpf, nome, nascimento, oculos in pessoas:
            print(f"CPF: {cpf} | Nome: {nome} | Nascimento: {nascimento} | Oculos: {oculos}")

        # -----------------------------------------------------
        # 5) UPDATE
        # Atualiza o nome da pessoa com base no CPF.
        # rowcount mostra quantas linhas foram afetadas.
        # -----------------------------------------------------
        cursor.execute(
            """
            UPDATE Pessoa
            SET nome = ?
            WHERE cpf = ?;
            """,
            ("Jose Silva", 20000000099),
        )

        conexao.commit()
        print(f"\nUPDATE realizado. Linhas afetadas: {cursor.rowcount}")

        # -----------------------------------------------------
        # 6) DELETE
        # Exemplo de exclusao de registro.
        # Deixei comentado para nao apagar automaticamente.
        # Se quiser testar, remova o comentario das linhas abaixo.
        # -----------------------------------------------------
        # cursor.execute("DELETE FROM Pessoa WHERE cpf = ?;", (20000000099,))
        # conexao.commit()
        # print(f"DELETE realizado. Linhas afetadas: {cursor.rowcount}")

    except sqlite3.DatabaseError as erro:
        # Captura erros relacionados ao banco de dados.
        print("Erro de banco de dados:", erro)

    finally:
        # Fecha cursor e conexao no final, mesmo se ocorrer erro.
        if cursor is not None:
            cursor.close()
        if conexao is not None:
            conexao.close()