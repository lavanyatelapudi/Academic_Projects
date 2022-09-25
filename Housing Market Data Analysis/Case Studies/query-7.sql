select avg(median_sale_price) as avg_sale_price,region 
as region from all_sales 
group by region limit 100;