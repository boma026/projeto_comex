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
            dataframes.append(df)
        else:
            print(f"Arquivo não encontrado: {caminho}")

    if dataframes:
        df_total = pd.concat(dataframes, ignore_index=True)
        engine = create_engine('sqlite:///database/comex.db')

        # 1. Inserir no banco
        df_total.to_sql('comex_detalhado', engine, if_exists='replace', index=False)

        # 2. Verificar qualidade após inserção
        verificar_qualidade_dados("comex_detalhado")

        print("ETL concluído.")
    else:
        print("Nenhum dado foi processado.")