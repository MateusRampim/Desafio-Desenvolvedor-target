SELECT c.id_cliente, c.razao, GROUP_CONCAT(t.numero ORDER BY t.numero SEPARATOR ', ') AS telefones
FROM clientes c
JOIN telefones t ON c.id_cliente = t.id_cliente
JOIN estados e ON c.id_estado = e.id_estado
WHERE e.sigla = 'SP'
GROUP BY c.id_cliente, c.razao;
