"Ler o arquivo csv com os dados do Base Varejo"

import pandas as pd
import os

PASTA = os.path.dirname(os.path.abspath(__file__))
CAMINHO_CSV_ORIGINAL = os.path.join(PASTA, "Base_Varejo_Limpa.csv")  
CAMINHO_CSV = os.path.join(PASTA, "Base_Varejo_Limpa.csv")

def carregar_dados():
    df = pd.read_csv(CAMINHO_CSV, sep=";", dtype=str)

    # Remove colunas vazias que aparecem no final do arquivo.
    df = df.dropna(axis=1, how="all")

    # Troca textos vazios ou com espaços por valores ausentes.
    df = df.replace(r"^\s*$", pd.NA, regex=True)

    # Converte o texto da coluna DATA para uma data do Python.
    df["DATA"] = pd.to_datetime(df["DATA"], format="%d/%m/%Y")

    # Preenche valores ausentes das outras colunas.
    for coluna in df.columns:
        if coluna != "DATA":
            df[coluna] = df[coluna].fillna("None")

    # Mantém apenas uma cópia de cada linha igual.
    df = df.drop_duplicates()

    return df


if __name__ == "__main__":
    df = carregar_dados()
    print(f"{len(df)} registros carregados.")
    print(df.head())
