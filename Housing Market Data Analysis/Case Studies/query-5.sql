select EXTRACT(year from period_begin) 
as year1, sum(pending_sales) 
as pending_sales_in_year,state
as state from all_sales 
group by year1, state;