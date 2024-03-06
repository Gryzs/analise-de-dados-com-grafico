# Importar a base de dados dos clientes
# Visualizar a base de dados
# Corrigir a base de dados
# Analise dos cancelamentos
# Analise da causa do cancelamento

# BIBLIOTECAS A SER UTILIZADA -> pip install pandas numpy openpyxl nbformat ipykernel plotly
# PANDAS -> Trabalhar com base de dados
# OPENPYXL -> Trabalhar com excel
# PLOTLY -> precisa do ipykernel e nbformat para funcionar e tem a função de mexer com gráficos

import pandas as pd

tabela = pd.read_csv("cancelamentos_sample.csv")

print(tabela)

# Coluna inutil -> Coluna que não faz importancia para a analise
tabela = tabela.drop(columns="CustomerID") # REMOVER COLUNA INUTIL

# tratar celulas vazias
print(tabela.info()) # VER INFOMAÇÃO DE QUANTAS CELULAS PREENCHIDAS NA TABELA
tabela = tabela.dropna() # TIRAR LINHAS QUE TENHA INFORMAÇÃO NULL
print(tabela.info()) # VER QUER AS INFOMAÇÕES NULL FOI DELETADO

# Analise dos cancelamentos
print(tabela["cancelou"].value_counts())