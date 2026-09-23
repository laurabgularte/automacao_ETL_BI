import pandas as pd
import requests
from datetime import datetime
try:
    from sqlalchemy import create_engine
except ImportError:
    create_engine = None


# CONFIGURAÇÕES DE CONEXÃO COM O BANCO

DB_USER = "seu_usuario"
DB_PASSWORD = "sua_senha"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "nome_do_banco"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def extrair_dados_api():
    """Extrai os dados brutos de uma API externa."""
    url = "https://api.exemplo.com/v1/dados"
    headers = {"Authorization": "Bearer SEU_TOKEN_AQUI"}
    
    resposta = requests.get(url, headers=headers)
    if resposta.status_code == 200:
        return pd.DataFrame(resposta.json())
    else:
        raise Exception(f"Erro ao acessar a API: {resposta.status_code} - {resposta.text}")

def transformar_dados(df):
    """Realiza a limpeza, tratamento e padronização dos dados."""
    # Remove registros duplicados
    df = df.drop_duplicates()
    
    # Adiciona carimbo de data/hora da sincronização
    df['data_atualizacao'] = datetime.now()
    
    # Padroniza tipos numéricos 
    if 'valor' in df.columns:
        df['valor'] = pd.to_numeric(df['valor'], errors='coerce')
        
    return df

def carregar_no_postgres(df):
    """Carrega a tabela tratada diretamente para o PostgreSQL."""
    if create_engine is None:
        raise ImportError(
            "SQLAlchemy não está instalado. Instale com: pip install sqlalchemy psycopg2-binary"
        )

    engine = create_engine(DATABASE_URL)
    
    # 'replace' substitui a tabela inteira a cada execução
    df.to_sql('tb_dados_api', engine, if_exists='replace', index=False)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Sincronização concluída com sucesso no PostgreSQL!")

if __name__ == "__main__":
    try:
        print("Iniciando o pipeline ETL...")
        df_bruto = extrair_dados_api()
        df_tratado = transformar_dados(df_bruto)
        carregar_no_postgres(df_tratado)
    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Falha na execução do pipeline: {e}")