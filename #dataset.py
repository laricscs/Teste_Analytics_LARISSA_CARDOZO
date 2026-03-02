#1 CRIAÇÃO DO DATASET

#importando as biblioteca i
import pandas as pd
import numpy as np 

np.random.seed(42) #seed - estado inicial para gerar uma sequência fixa de números aleatórios

n = 50  # Define a quantidade de registros do dataset

# Gera 50 datas entre 01/01/2023 e 31/12/2023
datas = pd.date_range(
    start="2023-01-01",
    end="2023-12-31",
    periods=n
)

# Lista de produtos disponíveis na loja
produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Impressora"]

# Define UMA categoria fixa para cada produto
categorias = {
    "Notebook": "Informática",
    "Monitor": "Informática",
    "Impressora": "Informática",
    "Mouse": "Acessórios",
    "Teclado": "Acessórios"
}

# Define UM preço fixo para cada produto
precos = {
    "Notebook": 4500.00,
    "Monitor": 1200.00,
    "Impressora": 950.00,
    "Mouse": 120.00,
    "Teclado": 250.00
}

# Sorteia os produtos das vendas
produto_sorteado = np.random.choice(produtos, n)

#criação do dataframe
df = pd.DataFrame({

    # ID único para cada venda
    "ID": range(1, n + 1),

    # Data em que a venda ocorreu
    "Data": datas,

    # Produto vendido, Sortea valores aleatórios
    "Produto": produto_sorteado,

    # Categoria do produto
    "Categoria": [categorias[p] for p in produto_sorteado],

    # Quantidade de itens vendidos em cada venda
    "Quantidade": np.random.randint(1, 7, n).astype(float),

    # Preço unitário do produto
    "Preço": [precos[p] for p in produto_sorteado]
})

# Exibe as primeiras linhas do dataset
print(df.head())


#INSERÇÃO DE ERROS NO DATASET

# Inserindo valor faltante (NaN) na coluna Preço
df.loc[3, "Preço"] = np.nan

# Inserindo valor faltante (NaN) na coluna Quantidade
df.loc[12, "Quantidade"] = np.nan

# Simula um registro duplicado:
# adiciona uma cópia da primeira linha ao final do DataFrame
df = pd.concat([df, df.iloc[[0]]], ignore_index=True) #reorganiza o índice

print(df.isnull().sum())


#2 LIMPEZA DOS DADOS

# Substitui valores nulos da coluna Preço
# usando o preço correto de cada produto
df["Preço"] = df["Preço"].fillna(
    df["Produto"].map(precos)
)

# Substitui valores nulos da coluna Quantidade
# pela mediana dos valores existentes
df["Quantidade"] = df["Quantidade"].fillna(
    df["Quantidade"].median()
)

#Remoção de registros duplicados
df.drop_duplicates(inplace=True)

#Conversão 

# Garante que a coluna Data esteja no formato datetime
df["Data"] = pd.to_datetime(df["Data"])

# Converte Quantidade para inteiro
df["Quantidade"] = df["Quantidade"].astype(int)

# Converte Preço para float e limita em 2 casas decimais
df["Preço"] = df["Preço"].astype(float).round(2)


# Salva o dataset limpo em um arquivo CSV
df.to_csv("data_clean.csv", index=False)
