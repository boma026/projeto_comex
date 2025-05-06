import pandas as pd
from sqlalchemy import create_engine
import os

def executar_etl():
    print("Iniciando processo ETL...")

    # Mapeamento de arquivos e tipo de operação
    arquivos = {
        'dados/IMP_2020.csv': 'Importação',
        'dados/IMP_2021.csv': 'Importação',
        'dados/EXP_2020.csv': 'Exportação',
        'dados/EXP_2021.csv': 'Exportação',
    }

    dataframes = []

    # Carregar arquivos CSV
    for caminho, tipo in arquivos.items():
        if os.path.exists(caminho):
            df = pd.read_csv(caminho, sep=';', encoding='latin1')
            df['Tipo'] = tipo
            dataframes.append(df)
        else:
            print(f"Arquivo não encontrado: {caminho}")

     # Concatenar todos os dataframes e salvar no banco
    if dataframes:
        df_total = pd.concat(dataframes, ignore_index=True)

        # Criar engine de conexão SQLite (dentro da pasta 'database/')
        engine = create_engine('sqlite:///database/comex.db')

        #inserir no banco de dados
        df_total.to_sql('comex_detalhado', engine, if_exists='replace', index=False)
        print("ETL concluído.")
    else:
        print("Nenhum dado foi processado.")