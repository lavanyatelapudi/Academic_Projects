use real_estate_db;
select EXTRACT(year from period_begin) as year1, count(*), property_type 
as year_value 
from time_period 
group by year1, property_type;
