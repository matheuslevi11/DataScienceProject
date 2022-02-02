import pandas as pd

def convert_float(numbers):
    converted = []
    for n in numbers:
        n = n.replace(',', '.').strip()
        converted.append(float(n))

    return pd.Series(converted)

def strip_dataframe(df, columns):
    for col in columns:
        stripped = []
        for string in df[col]:
            stripped.append(string.strip())
        df[col] = pd.Series(stripped)
    return df

def tratamento_abono(filename):
    column_names = ['nome', 'CPF', 'descricao_cargo', 'escolaridade', 'orgao_atuacao', 'UPAG', 'unidade_organizacional',
    'UF_residencia', 'cidade_residencia', 'situacao', 'anos_servico', 'meses_servico', 'ano/mes_inicio', 'valor_abono']

    df = pd.read_csv(f"../AbonoPermanenciaDatabases/ABONOP_{filename}.csv", sep=';', index_col=False, encoding='cp860')
    df.columns = column_names


    df.valor_abono = convert_float(df.valor_abono)


    string_columns = ['nome', 'descricao_cargo', 'escolaridade', 'orgao_atuacao', 'UPAG', 'unidade_organizacional',
    'UF_residencia', 'cidade_residencia', 'situacao']

    df = strip_dataframe(df, string_columns)
    df = df.drop_duplicates()

    return df
