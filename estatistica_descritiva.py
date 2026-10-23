"""Estatísticas simples da quantidade de filhos dos clientes."""

import pandas as pd

from carregar_dados import carregar_dados


def analisar_numero_filhos():
    df = carregar_dados()

    # Cada cliente aparece em várias compras, então usamos uma linha por cliente.
    clientes = df.drop_duplicates(subset="CL_ID")

    # Transforma os valores da coluna em números.
    numero_filhos = pd.to_numeric(clientes["CL_FHL"], errors="coerce")

    # Ignora valores que não puderam ser convertidos.
    numero_filhos = numero_filhos.dropna()

    if numero_filhos.empty:
        raise ValueError("Não existem valores para analisar na coluna CL_FHL.")

    print("Estatísticas da quantidade de filhos:")
    print(f"Quantidade de registros: {numero_filhos.count()}")
    print(f"Média: {numero_filhos.mean():.2f}")
    print(f"Mediana: {numero_filhos.median():.2f}")
    print(f"Moda: {numero_filhos.mode().tolist()}")
    print(f"Mínimo: {numero_filhos.min()}")
    print(f"Máximo: {numero_filhos.max()}")
    print(f"Desvio padrão: {numero_filhos.std():.2f}")


if __name__ == "__main__":
    analisar_numero_filhos()
