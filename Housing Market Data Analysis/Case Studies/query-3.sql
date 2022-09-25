select EXTRACT(year from period_begin) 
as year1, sum(homes_sold) as homes_sold_in_year, property_type
as prop_type 
from all_sales 
group by year1, property_type;