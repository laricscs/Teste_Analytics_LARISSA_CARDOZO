#
# Total de vendas por produto e categoria
SELECT
    Produto,
    Categoria,
    SUM(Quantidade * Preço) AS Total_Vendas
FROM vendas

-- Agrupa os dados por produto e categoria
GROUP BY Produto, Categoria

-- Ordena do maior para o menor valor total de vendas
ORDER BY Total_Vendas DESC;




# Produtos que venderam menos em junho de 2023
-- PARTE 2 - CONSULTAS SQL
-- Análise de Vendas

-- 1. Total de vendas por produto e categoria
SELECT
    Produto,
    Categoria,
    SUM(Quantidade * Preço) AS Total_Vendas
FROM vendas
GROUP BY Produto, Categoria
ORDER BY Total_Vendas DESC;

-- 2. Produtos que venderam menos em junho de 2023
SELECT
    Produto,
    SUM(Quantidade * Preço) AS Total_Vendas_Junho
FROM vendas
WHERE Data >= '2023-06-01'
  AND Data < '2023-07-01'
GROUP BY Produto
ORDER BY Total_Vendas_Junho ASC;