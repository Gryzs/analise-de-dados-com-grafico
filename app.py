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
import plotly.express as px

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

print(tabela["cancelou"].value_counts(normalize=True)) # PORCENTUAL

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou") # CRIAR GRAFICO

    grafico.show() # MOSTRAR GRAFICO

tabela = tabela[tabela["duracao_contrato"]!="Monthly"] # sem duração do contrato mensal
tabela = tabela[tabela["ligacoes_callcenter"]<=4] # sem ligação do call center de 4 vezes
tabela = tabela[tabela["dias_atraso"]<=20] # sem atraso de pagamento maior do que 20 dias

print(tabela["cancelou"].value_counts(normalize=True))