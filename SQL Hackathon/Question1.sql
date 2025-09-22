Select s.category_id, p.product_name, SUM(s.sales_amount) as total_sales From sales s Join products p on s.product_id = p.product_id group by  s.category_id, p.product_name
having SUM(s.sales_amount) = (
    select MAX(total_sales)
    from (
        select category_id, product_id, SUM(sales_amount) as total_sales
        from sales
        group by category_id, product_id
    ) sub
    where sub.category_id = s.category_id
);
