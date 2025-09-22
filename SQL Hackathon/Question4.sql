Select region, customer_id, count(*) as total_orders From orders Group by region, customer_id having count(*) = (
    select max(order_count)
    from (
        select region as r, customer_id as c, COUNT(*) as order_count
        from orders
        where region = orders.region
        group by region, customer_id
    ) sub
    where sub.r = orders.region
);
