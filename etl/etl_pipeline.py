import pandas as pd
from sqlalchemy import create_engine
import os
from etl.verificacao_qualidade import verificar_qualidade_dados

def executar_etl():
    print("Iniciando processo ETL...")

    arquivos = {
        'dados/IMP_2020.csv': 'Importação',
        'dados/IMP_2021.csv': 'Importação',
        'dados/EXP_2020.csv': 'Exportação',
        'dados/EXP_2021.csv': 'Exportação',
    }

    dataframes = []

    for caminho, tipo in arquivos.items():

        if os.path.exists(caminho):
            df = pd.read_csv(caminho, sep=';', encoding='latin1')
            df['Tipo'] = tipo
            print(f"✅ Arquivo carregado: {caminho} ({len(df)} linhas)")
            dataframes.append(df)
        else:

            print(f"❌ Arquivo não encontrado: {caminho}")

    if dataframes:
        df_total = pd.concat(dataframes, ignore_index=True)

        # Tratamento de dados
        df_total['VL_FRETE'] = df_total['VL_FRETE'].fillna(0.0)
        df_total['VL_SEGURO'] = df_total['VL_SEGURO'].fillna(0.0)
        df_total = df_total[df_total['VL_FOB'] > 0]

        # Garante que a pasta 'database/' exista
        os.makedirs('database', exist_ok=True)

        engine = create_engine('sqlite:///database/comex.db')
        print(f"Conectando ao banco: {engine}")

        # Mostrar tabelas existentes antes da inserção
        with engine.connect() as conn:
            tabelas = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
            print("Tabelas no banco de dados:")
            print(tabelas)

        # Inserir dados tratados no banco
        df_total.to_sql('comex_detalhado', engine, if_exists='replace', index=False)
        print(f"✅ Dados inseridos no banco (total de {len(df_total)} linhas).")

        # Verificação de qualidade
        verificar_qualidade_dados("comex_detalhado")

        print("ETL concluído.")
    else:
        print("❌ Nenhum dado foi processado.")
