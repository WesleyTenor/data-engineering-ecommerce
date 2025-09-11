-- Total de pedidos por status
SELECT order_status, COUNT(*) 
FROM raw.orders 
GROUP BY order_status;

-- Ticket médio por cliente
SELECT c.customer_unique_id, AVG(p.payment_value) as avg_ticket
FROM raw.customers c
JOIN raw.orders o ON c.customer_id = o.customer_id
JOIN raw.payments p ON o.order_id = p.order_id
GROUP BY c.customer_unique_id
ORDER BY avg_ticket DESC
LIMIT 10;
