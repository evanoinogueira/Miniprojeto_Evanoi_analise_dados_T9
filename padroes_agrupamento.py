"""Agrupamentos simples dos dados da tabela de varejo."""

import pandas as pd

from carregar_dados import carregar_dados


def mostrar_agrupamentos():
    # Carrega os dados que já foram limpos.
    df = carregar_dados()

    print("\n" + "=" * 60)
    print("SPRINT 5 - PADRÕES DE AGRUPAMENTO")
    print("=" * 60)

    # Conta quantos registros existem em cada categoria.
    registros_categoria = df.groupby("PR_CAT").size().sort_values(ascending=False)
    print("\nQuantidade de registros por categoria:")
    print(registros_categoria)

    # Conta quantos registros existem para cada gênero.
    registros_genero = df.groupby("CL_GENERO").size().sort_values(ascending=False)
    print("\nQuantidade de registros por gênero:")
    print(registros_genero)

    # Mostra a quantidade de registros por gênero e categoria.
    tabela_genero_categoria = pd.crosstab(df["CL_GENERO"], df["PR_CAT"])
    print("\nQuantidade por gênero e categoria:")
    print(tabela_genero_categoria)


if __name__ == "__main__":
    mostrar_agrupamentos()
