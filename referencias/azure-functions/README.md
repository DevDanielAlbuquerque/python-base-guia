# Referência histórica — Azure Functions e Telegram

Exemplo comentado preservado durante a organização do guia. Utiliza Azure Functions, SQL Server via pymssql e a API do Telegram; não é um exemplo de SQLite.

Este código está fora da sequência de fundamentos e não é uma aplicação pronta para implantação. Depende de serviços externos e das variáveis DB_SERVER, DB_USER, DB_PASSWORD, DB_NAME, TELEGRAM_TOKEN e TELEGRAM_CHAT_ID.

Limitação conhecida: a rotina pode atualizar a data do último envio mesmo sem confirmação de sucesso do Telegram. Há também requisição sem timeout e tratamento de fuso horário por ajuste manual. Esses pontos precisam de revisão antes de reutilizar o código.

Não foi executado com serviços reais nesta revisão. Não armazene credenciais no repositório.
