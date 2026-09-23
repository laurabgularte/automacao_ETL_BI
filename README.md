# Automação ETL: API para PostgreSQL (Power BI)

Este repositório contém um script em Python estruturado para automatizar o fluxo de **ETL (Extração, Transformação e Carga)**. O objetivo é buscar dados atualizados de uma API, realizar o tratamento e a limpeza utilizando a biblioteca `pandas`, e persistir os dados consolidados em um banco de dados **PostgreSQL**, servindo de fonte otimizada para relatórios do **Power BI**.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas** (Manipulação e tratamento de dados)
- **Requests** (Requisições HTTP para a API)
- **SQLAlchemy & Psycopg2** (Conexão e carga no PostgreSQL)

---

## ⚙️ Pré-requisitos e Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/laurabgularte/automacao_ETL_BI.git
   cd seu-repositorio
   ```

2. Instale as dependências necessárias executando:
   ```bash
   pip install pandas requests sqlalchemy psycopg2-binary
   ```

---

## 🚀 Como Configurar e Executar

1. Abra o arquivo `pipeline_etl.py`.
2. Configure as credenciais do seu banco de dados PostgreSQL nas variáveis correspondentes (`DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_NAME`).
3. Atualize a URL da API e o token de acesso na função `extrair_dados_api()`.
4. Execute o script via terminal:
   ```bash
   python pipeline_etl.py
   ```

---

## 📊 Integração com o Power BI

1. Abra o **Power BI Desktop**.
2. Clique em **Obter Dados** e selecione o conector **Banco de Dados PostgreSQL**.
3. Insira as credenciais do seu banco.
4. Selecione a tabela gerada pelo script (`tb_dados_api`). Como os dados já chegam limpos e tipados, você garante um relatório de alta performance.

---

## ⏰ Agendamento (Automação)

Para manter o seu relatório sempre atualizado, você pode configurar este script para rodar de forma autônoma:

- No **Windows**: Utilize o _Agendador de Tarefas_.
- No **Linux/macOS**: Configure uma rotina no _Crontab_.
