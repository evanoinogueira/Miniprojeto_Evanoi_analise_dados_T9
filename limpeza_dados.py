from pathlib import Path

import pandas as pd


class LimpezaDados:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.registros_iniciais = len(self.df)

    def remover_colunas_vazias(self):
        campos_vazios = self.df.astype("string").apply(
            lambda coluna: coluna.str.fullmatch(r"\s*").fillna(False)
        )
        self.df = self.df.mask(campos_vazios)
        self.df = self.df.dropna(axis=1, how="all")
        return self

    def remover_nulos(self):
        self.df = self.df.dropna()
        return self

    def remover_duplicados(self):
        self.df = self.df.drop_duplicates().reset_index(drop=True)
        return self

    def executar(self):
        self.remover_colunas_vazias().remover_nulos().remover_duplicados()
        return self.df

    def salvar_csv(self, caminho_saida):
        self.df.to_csv(caminho_saida, index=False, sep=";")
        return self

    def mostrar_relatorio(self):
        print(f"Registros iniciais: {self.registros_iniciais}")
        print(f"Registros finais: {len(self.df)}")
        print(f"Registros removidos: {self.registros_iniciais - len(self.df)}")


if __name__ == "__main__":
    from carregar_dados import CAMINHO_CSV_ORIGINAL

    caminho_saida = Path(CAMINHO_CSV_ORIGINAL).with_name("Base_Varejo_Limpa.csv")
    limpeza = LimpezaDados(
        pd.read_csv(CAMINHO_CSV_ORIGINAL, sep=";", dtype=str)
    )
    limpeza.executar()
    limpeza.mostrar_relatorio()
    limpeza.salvar_csv(caminho_saida)
    print(f"Base_Varejo_Limpa.csv em: {caminho_saida}")