"Ler o arquivo csv com os dados do Base Varejo"

import pandas as pd

CAMINHO_CSV = "Base Varejo.csv"

def carregar_dados():
    df = pd.read_csv(CAMINHO_CSV, dtype={"CNPJ": str, "CNAE": str, "CEP": str})
    return df

if __name__ == "__main__":
    df = carregar_dados()
    print(f"{len(df)} registros carregados.")
    print(df.head())
