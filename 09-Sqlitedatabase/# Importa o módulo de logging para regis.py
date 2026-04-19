# Importa o módulo de logging para registrar mensagens de debug, info e erros
import logging

# Importa o SDK do Azure Functions para criar funções serverless
import azure.functions as func

# Importa o módulo os para acessar variáveis de ambiente do sistema
import os

# Importa o driver pymssql para conectar ao banco de dados SQL Server
import pymssql

# Importa a biblioteca requests para fazer requisições HTTP (chamada à API do Telegram)
import requests

# Importa datetime para trabalhar com datas/horas e timedelta para calcular diferenças de tempo
from datetime import datetime, timedelta

# Cria a instância principal do Azure Functions App (ponto de entrada da aplicação)
app = func.FunctionApp()


# ─────────────────────────────────────────────
# 🔌 FUNÇÃO: CONEXÃO COM BANCO DE DADOS
# ─────────────────────────────────────────────
def conectar_sql():
    # Abre e retorna uma conexão com o SQL Server usando credenciais armazenadas em variáveis de ambiente
    return pymssql.connect(
        server=os.getenv("DB_SERVER"),      # Endereço/hostname do servidor SQL (ex: "meuservidor.database.windows.net")
        user=os.getenv("DB_USER"),          # Usuário do banco de dados
        password=os.getenv("DB_PASSWORD"),  # Senha do banco de dados
        database=os.getenv("DB_NAME")       # Nome do banco de dados a ser usado
    )


# ─────────────────────────────────────────────
# 📩 FUNÇÃO: ENVIO DE MENSAGEM VIA TELEGRAM
# ─────────────────────────────────────────────
def enviar_telegram(mensagem):
    # Lê o token do bot do Telegram a partir da variável de ambiente
    token = os.getenv("TELEGRAM_TOKEN")

    # Lê o ID do chat/grupo que receberá a mensagem
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    # Valida se as variáveis foram configuradas; se não, loga erro e encerra a função
    if not token or not chat_id:
        logging.error("❌ TELEGRAM_TOKEN ou TELEGRAM_CHAT_ID não definidos")
        return  # Sai da função sem enviar nada

    # Monta a URL da API do Telegram usando o token do bot
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    # Cria o dicionário (payload) com os dados da mensagem a ser enviada
    payload = {
        "chat_id": chat_id,   # Destinatário da mensagem
        "text": mensagem      # Conteúdo da mensagem
    }

    try:
        # Faz a requisição HTTP POST para a API do Telegram enviando o payload
        response = requests.post(url, data=payload)

        # Loga o código de status retornado pela API (200 = sucesso)
        logging.info(f"📡 Telegram status: {response.status_code}")

        # Loga o corpo completo da resposta da API para diagnóstico
        logging.info(f"📡 Telegram resposta: {response.text}")

    except Exception as e:
        # Em caso de falha na requisição, loga a mensagem de erro
        logging.error(f"❌ ERRO TELEGRAM: {str(e)}")


# ─────────────────────────────────────────────
# ⏰ FUNÇÃO PRINCIPAL — AGENDADA (TIMER TRIGGER)
# ─────────────────────────────────────────────

# Decorator que define o agendamento via cron: executa todo dia às 11:00 UTC
# "0 0 11 * * *" → segundo=0, minuto=0, hora=11, qualquer dia/mês/dia-da-semana
# run_on_startup=False → NÃO executa automaticamente ao iniciar a aplicação
@app.timer_trigger(schedule="0 0 11 * * *", arg_name="myTimer", run_on_startup=False)
def alerta_manha(myTimer: func.TimerRequest) -> None:
    # Loga o início da execução da função
    logging.info("🚀 Executando alertas...")

    # ── AJUSTE DE FUSO HORÁRIO (Brasil = UTC-3) ──────────────────────────────
    # Obtém o horário atual em UTC e subtrai 3 horas para converter para horário de Brasília
    agora = datetime.utcnow() - timedelta(hours=3)

    # Extrai apenas a data (sem hora) do horário atual no fuso de Brasília
    hoje = agora.date()

    # Extrai apenas a hora do horário atual (inteiro, ex: 14 para 14h)
    hora = agora.hour

    # ── BLOQUEIOS DE EXECUÇÃO ─────────────────────────────────────────────────

    # weekday() retorna 0=segunda ... 4=sexta, 5=sábado, 6=domingo
    # Se for final de semana (>= 5), encerra a função sem processar nada
    if agora.weekday() >= 5:
        logging.info("⛔ Final de semana - ignorando execução")
        return  # Encerra a função imediatamente

    # Se a hora atual estiver fora do horário comercial (antes das 8h ou depois das 18h), encerra
    if hora < 8 or hora > 18:
        logging.info("⛔ Fora do horário comercial")
        return  # Encerra a função imediatamente

    # ── CONEXÃO COM O BANCO ───────────────────────────────────────────────────
    try:
        # Chama a função conectar_sql() e armazena a conexão
        conn = conectar_sql()

        # Cria um cursor para executar comandos SQL na conexão aberta
        cursor = conn.cursor()

        # Loga sucesso na conexão
        logging.info("✅ Conectou no banco")

    except Exception as e:
        # Se a conexão falhar, loga o erro e encerra a função para não continuar sem banco
        logging.error(f"❌ ERRO SQL: {str(e)}")
        return  # Encerra a função imediatamente

    # ── BUSCAR ALERTAS PENDENTES ──────────────────────────────────────────────

    # Executa a query SQL buscando todos os alertas com status 'PENDENTE'
    cursor.execute("""
        SELECT id, descricao, data_vencimento, data_lembrete, data_ultimo_envio
        FROM alertas_dev
        WHERE status = 'PENDENTE'
    """)

    # Recupera todos os registros retornados pela query como lista de tuplas
    registros = cursor.fetchall()

    # Loga quantos registros foram encontrados
    logging.info(f"📊 Registros encontrados: {len(registros)}")

    # ── PROCESSA CADA ALERTA ──────────────────────────────────────────────────

    # Itera sobre cada linha (tupla) retornada pelo banco
    for row in registros:
        # Mapeia cada posição da tupla para uma variável com nome descritivo
        id_alerta = row[0]          # ID único do alerta no banco
        descricao = row[1]          # Texto descritivo do alerta
        data_vencimento = row[2]    # Data limite/prazo final do alerta
        data_lembrete = row[3]      # Data a partir da qual o lembrete deve ser enviado
        data_ultimo_envio = row[4]  # Data em que o último alerta foi enviado (pode ser None)

        # ── NORMALIZAÇÃO DAS DATAS ────────────────────────────────────────────
        # O banco pode retornar datetime (com hora) ou date (só data)
        # hasattr verifica se o objeto tem o método .date() — se sim, é um datetime
        if hasattr(data_vencimento, "date"):
            data_vencimento = data_vencimento.date()  # Converte datetime → date

        if hasattr(data_lembrete, "date"):
            data_lembrete = data_lembrete.date()  # Converte datetime → date

        # ── VERIFICAÇÃO: JÁ ENVIOU HOJE? ─────────────────────────────────────
        # Só entra no bloco se data_ultimo_envio não for None/vazio
        if data_ultimo_envio:
            # Normaliza data_ultimo_envio para tipo date se for datetime
            data_envio = data_ultimo_envio.date() if hasattr(data_ultimo_envio, "date") else data_ultimo_envio

            # Se o último envio foi hoje, pula para o próximo registro sem enviar de novo
            if data_envio == hoje:
                logging.info(f"⏭️ Já enviado hoje: {descricao}")
                continue  # Vai para a próxima iteração do for

        # ── VERIFICAÇÃO: ESTÁ NA DATA DE LEMBRETE? ───────────────────────────
        # Só envia se a data de hoje for igual ou posterior à data de lembrete configurada
        if hoje >= data_lembrete:
            # Calcula quantos dias restam até o vencimento (pode ser negativo se já venceu)
            dias_restantes = (data_vencimento - hoje).days

            # Define a mensagem de acordo com a situação do prazo
            if dias_restantes < 0:
                # Alerta já passou da data de vencimento → está atrasado
                mensagem = f"🚨 ATRASADO!\n📌 {descricao}"
            elif dias_restantes == 0:
                # Alerta vence exatamente hoje
                mensagem = f"🚨 PRAZO FINAL HOJE\n📌 {descricao}"
            else:
                # Alerta ainda está dentro do prazo, informa quantos dias restam
                mensagem = f"📌 Lembrete\n{descricao}\n⏳ {dias_restantes} dias restantes"

            # Chama a função de envio passando a mensagem montada acima
            enviar_telegram(mensagem)

            # Atualiza o campo data_ultimo_envio no banco com a data/hora atual do servidor SQL
            cursor.execute("""
                UPDATE alertas_dev
                SET data_ultimo_envio = GETDATE()
                WHERE id = %s
            """, (id_alerta,))  # %s é o placeholder seguro contra SQL Injection no pymssql

            # Confirma (persiste) a atualização no banco de dados
            conn.commit()

            # Loga que o registro foi atualizado com sucesso
            logging.info(f"✅ Atualizado envio: {descricao}")

    # Fecha a conexão com o banco ao terminar de processar todos os registros
    conn.close()