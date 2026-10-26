# Mini-Projeto — Análise Exploratória de Dados (Varejo)

**Aluno:** Evanói Alexandre Nogueira

**Turma:** Análise de Dados com Python T9

**Tipo:** Mini-projeto avaliativo

## Sobre o projeto

O projeto carrega uma base de varejo em CSV, remove duplicatas exatas ao
carregá-la e apresenta estatísticas da quantidade de filhos dos clientes e
contagens agrupadas por categoria e gênero.

## Arquivos

- `Base_Varejo.csv`: base original.
- `Base_Varejo_Limpa.csv`: base limpa utilizada pelos scripts de análise.
- `carregar_dados.py`: leitura e preparação da base limpa.
- `limpeza_dados.py`: funções para remover colunas vazias, registros nulos e
  linhas duplicadas.
- `estatistica_descritiva.py`: estatísticas da quantidade de filhos por cliente.
- `padroes_agrupamento.py`: contagens por categoria, gênero e cruzamento entre
  gênero e categoria.
- `formatacao.py`: funções auxiliares para limpar e formatar valores.
- `requirements.txt`: dependências Python externas.

## Requisitos

- Python 3 instalado.
- Terminal PowerShell ou Prompt de Comando do Windows.
- Os arquivos CSV na mesma pasta dos scripts.

As dependências externas listadas em `requirements.txt` são:

- `pandas`: leitura e análise dos dados.
- `rich`: listado no arquivo de dependências, mas não é utilizado atualmente
  pelos scripts do projeto.

`os`, `pathlib`, `re` e `datetime` também são usados, mas fazem parte da
biblioteca padrão do Python e não precisam ser instalados com `pip`.

## Como instalar e executar (PowerShell)

Abra o PowerShell na pasta do projeto e execute:

```powershell
# Cria um ambiente virtual local
python -m venv .venv

# Ativa o ambiente virtual
.\.venv\Scripts\Activate.ps1

# Instala as dependências listadas no projeto
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Confirma a leitura da base limpa
python .\carregar_dados.py

# Executa a análise descritiva da quantidade de filhos
python .\estatistica_descritiva.py

# Executa os agrupamentos por categoria e gênero
python .\padroes_agrupamento.py
```

Se o PowerShell bloquear a ativação do ambiente, permita scripts apenas na
sessão atual e tente ativá-lo novamente:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Também é possível executar os scripts sem ativar o ambiente, usando
`.\.venv\Scripts\python.exe` no lugar de `python`.

## Observação sobre a etapa de limpeza

Os scripts de análise leem `Base_Varejo_Limpa.csv`. Esse arquivo já está
incluído no projeto, então não é necessário executar `limpeza_dados.py` para
gerar as análises.

No estado atual do código, `CAMINHO_CSV_ORIGINAL` em `carregar_dados.py`
também aponta para `Base_Varejo_Limpa.csv`. Por isso, executar
`python .\limpeza_dados.py` não processa `Base_Varejo.csv`: reprocessa e grava
por cima do arquivo limpo. Faça uma cópia de segurança antes de executar essa
etapa.

## Insights observados na base limpa

Os números abaixo foram calculados a partir de `Base_Varejo_Limpa.csv`.
As contagens por categoria e gênero representam **linhas/registros**, não
faturamento, quantidade de unidades vendidas ou clientes distintos.

- A base contém **733.447 registros**, **1.000 clientes distintos** e **18.471
  valores distintos de `CO_ID`**.
- **Alimentos** é a categoria com mais registros: **384.197 (52,38%)**.
  Em seguida vêm **Higiene** com **137.702 (18,77%)** e **Limpeza** com
  **128.632 (17,54%)**.
- Há **3.228 registros (0,44%)** com a categoria `#N/D`, indicando uma
  classificação ausente ou não identificada.
- Nos registros com gênero informado, **F** corresponde a **382.427 (52,14%)**
  e **M** a **351.020 (47,86%)**. Essa comparação é por linha, não por cliente.
- Considerando um registro por cliente, **527 dos 1.000 clientes (52,7%)**
  têm zero filhos. Por isso, tanto a mediana quanto a moda são **0**. A média
  é **1,14 filho por cliente**.
- A comparação da base original com a limpa identificou **96.553 linhas
  exatamente duplicadas** removidas. Isso não significa que sejam compras
  repetidas: `CO_ID` pode aparecer em várias linhas, por exemplo, para
  diferentes itens da mesma compra.
- Os registros cobrem o período de **04/01/2019 a 08/12/2022**.

## Limitações

Os scripts atuais não calculam faturamento nem ticket médio, pois a base usada
na análise não possui uma coluna de preço ou valor de venda. As análises de
categoria e gênero contam linhas da base, e não vendas únicas ou clientes
únicos. A categoria `#N/D` também permanece nos dados e deve ser considerada
ao interpretar os agrupamentos.
