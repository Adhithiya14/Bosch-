Select category_id, avg(price) as avg_price from products Group by category_id having avg(price) > (select avg(price) from products);
