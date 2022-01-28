import pandas as pd

column_names = ['nome', 'CPF', 'matricula', 'nome_orgao', 'sigla_orgao', 'codigo_orgao', 'desc_cargo', 'classe_cargo',
'padrao_cargo', 'ref_cargo', 'nivel_cargo', 'tipo_aposentadoria', 'fundamentacao', 'ato_aposentadoria', 'data_aposentadoria',
'tipo_ingresso', 'data_ingresso', 'valor_aposentadoria']

def strip_dataframe(df, columns):
    for col in columns:
        stripped = []
        for string in df[col]:
            stripped.append(string.strip())
        df[col] = pd.Series(stripped)
    return df

def convert_float(numbers):
    converted = []
    for n in numbers:
        n = n.replace('.', '').strip()
        n = n.replace(',', '.')
        converted.append(float(n))

    return pd.Series(converted)

def parse_date(dates):
    parsed = []
    for date in dates:
        date = str(date)
        if len(date) == 8:
            day = date[0] + date[1]
            month = date[2] + date[3]
            year = date[4] + date[5] + date[6] + date[7]
        else:
            day = '0' + date[0]
            month = date[1] + date[2]
            year = date[3] + date[4] + date[5] + date[6]
        parsed.append(year+'-'+month+'-'+day)
    return pd.Series(parsed) 

def tratamento_aposentados(filename):
    string_columns = ['nome', 'CPF', 'nome_orgao', 'sigla_orgao', 'desc_cargo', 'classe_cargo',
    'padrao_cargo', 'tipo_aposentadoria', 'fundamentacao', 'ato_aposentadoria']

    df = pd.read_csv(f"../AposentadosDatabases/APOSENTADOS_{filename}.csv", sep=';', index_col=False, encoding='cp860', names=column_names)

    df = strip_dataframe(df, string_columns)

    df.valor_aposentadoria = convert_float(df.valor_aposentadoria)

    df.data_aposentadoria = parse_date(df.data_aposentadoria)
    df.data_aposentadoria = pd.to_datetime(df.data_aposentadoria)

    df.data_ingresso = parse_date(df.data_ingresso)
    df.data_ingresso = pd.to_datetime(df.data_ingresso)

    df['data_aposentadoria'] = df['data_aposentadoria'].dt.date
    df['data_ingresso'] = df['data_ingresso'].dt.date
    return df


