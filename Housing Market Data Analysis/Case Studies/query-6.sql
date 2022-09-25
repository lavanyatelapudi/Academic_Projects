select EXTRACT(year from period_begin) 
as year1, sum(new_listings) 
as new_listings_in_year,region 
as region from all_sales 
group by year1, region;