select EXTRACT(year from period_begin) 
as year_value, sum(homes_sold) 
as homes_sold_in_year, region
as region_name from all_sales 
group by year_value, region;