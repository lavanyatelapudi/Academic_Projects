select avg(median_list_price) 
as avg_list_price,region 
as region from all_sales 
group by region limit 100;