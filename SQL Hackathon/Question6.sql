Select p.product_id, p.product_name From products p left join orders o on p.product_id = o.product_id where o.product_id is null;
