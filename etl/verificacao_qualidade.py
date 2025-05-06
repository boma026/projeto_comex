import pandas as pd
from sqlalchemy import create_engine

def verificar_qualidade_dados(nome_tabela, caminho_banco='comex.db'):
    engine = create_engine(f'sqlite:///{caminho_banco}')
    with engine.connect() as conn:
        df = pd.read_sql(f"SELECT * FROM {nome_tabela}", conn)

    print(f"\n📊 Verificando qualidade dos dados da tabela: {nome_tabela}")

    # Verificar valores nulos
    print("\n🔍 Valores nulos (apenas colunas com nulos):")
    nulos = df.isnull().sum()
    print(nulos[nulos > 0] if not nulos[nulos > 0].empty else "Nenhum valor nulo encontrado.")

    # Tipos de dados
    print("\n🔍 Tipos de dados das colunas:")
    print(df.dtypes)

    # Linhas duplicadas
    print(f"\n🔍 Linhas totalmente duplicadas: {df.duplicated().sum()}")

    # Verificar se existem valores inválidos em colunas específicas
    if 'CO_MES' in df.columns:
        meses_invalidos = df[~df['CO_MES'].between(1, 12)]
        print(f"\n🔍 Meses inválidos (fora de 1-12): {len(meses_invalidos)}")

    if 'VL_FOB' in df.columns:
        valores_negativos = df[df['VL_FOB'] < 0]
        print(f"\n🔍 Valores negativos em VL_FOB: {len(valores_negativos)}")

    # Tipos esperados (opcional, para verificação de schema)
    tipos_esperados = {
        'CO_ANO': 'int64',
        'CO_MES': 'int64',
        'SG_UF': 'object',
        'VL_FOB': 'float64',
    }
    print("\n🔍 Comparando tipos esperados (se as colunas existirem):")
    for col, tipo in tipos_esperados.items():
        if col in df.columns:
            tipo_atual = df[col].dtype
            if tipo_atual != tipo:
                print(f"⚠️ Coluna '{col}' tem tipo '{tipo_atual}', esperado: '{tipo}'")
        else:
            print(f"⚠️ Coluna esperada '{col}' não encontrada no dataframe.")

    print("\n✅ Verificação de qualidade concluída.\n")