import pandas as pd
from sqlalchemy import create_engine

def verificar_qualidade_dados(nome_tabela):
    print(f"\nConsultando a tabela: {nome_tabela}")

    engine = create_engine('sqlite:///database/comex.db')
    with engine.connect() as conn:
        df = pd.read_sql(f"SELECT * FROM {nome_tabela}", conn)

    print("\n📌 Dados faltantes por coluna:")
    print(df.isnull().sum())

    print("\n📌 Tipos de dados das colunas:")
    print(df.dtypes)

    print("\n📌 Registros duplicados:", df.duplicated().sum())

    print("\n📌 Valores únicos para CO_PAIS:", df['CO_PAIS'].nunique())
    print("📌 Valores únicos para CO_NCM:", df['CO_NCM'].nunique())

    print("\n📌 Verificação de anos válidos:")
    anos_validos = df['CO_ANO'].isin([2020, 2021])
    print(f"Linhas com anos válidos (2020 ou 2021): {anos_validos.sum()} de {len(df)}")

    print("\n📌 Verificação de VL_FOB:")
    fob_invalidos = (df['VL_FOB'] <= 0).sum()
    if fob_invalidos == 0:
        print("✅ Todos os valores de FOB são positivos.")
    else:
        print(f"⚠️ Há {fob_invalidos} registros com VL_FOB inválido (<= 0)")

    print("\n📌 Estatísticas de VL_FRETE e VL_SEGURO:")
    print("Frete:")
    print(df['VL_FRETE'].describe())
    print("Seguro:")
    print(df['VL_SEGURO'].describe())
    
