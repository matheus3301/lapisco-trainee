SELECT n.nome_novela
FROM tbNovela n
INNER JOIN tbCapitulo c 
ON n.codigo_novela = c.codigo_novela
GROUP BY c.codigo_novela
HAVING COUNT(*) > 40;