SELECT n.nome_novela, COUNT(*) as qtd_capitulos
FROM tbNovela n
INNER JOIN tbCapitulo c 
ON n.codigo_novela = c.codigo_novela
GROUP BY c.codigo_novela;