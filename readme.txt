# Mini-Projeto — Análise Exploratória de Dados (Varejo)
**Aluno:** [Seu Nome]
**Turma:** Análise de Dados T1
**Como executar:** Abra no VSCode e rode `python miniprojeto_varejo.py`
(ou abra no Google Colab e execute todas as células).

## 🧠 Reflexão Teórica — ETL e Qualidade de Dados
ETL (Extract, Transform, Load) é o processo de extrair dados brutos,
transformá-los (limpeza, tipagem, enriquecimento) e carregá-los em um
formato adequado para análise. Neste projeto, aplicamos ETL ao:
- **Extrair** o CSV com `csv.DictReader` (leitura nativa estruturada);
- **Transformar** tipos (str → int/float/datetime), tratar nulos e
  padronizar categorias vazias como "Sem Categoria";
- **Carregar** a base limpa em `output/df_limpo.csv`.

Qualidade de dados é fundamental porque "lixo entra, lixo sai": dados
duplicados, nulos mal tratados ou datas inválidas geram indicadores
enganosos e decisões erradas. Por isso, validar identificadores únicos
(ex.: Id_Compra) e justificar cada imputação (mediana, moda) é parte
essencial do trabalho analítico.

## 💡 Insights da Análise 
1. A categoria X concentra a maior parte do faturamento.
2. O gênero Y representa a maioria das compras em volume.
3. A mediana de número de filhos é [valor], indicando perfil familiar [Z].
4. Foram identificadas [N] duplicatas de Id_Compra antes da limpeza.
5. [Insight sobre sazonalidade ou ticket médio, se aplicável.]
6. Problema remanescente: [ex.: datas fora do padrão em X% dos registros].