select EXTRACT(year from period_begin) as year1, sum(new_listings)
 as new_listings, property_type 
 as prop_type from all_sales 
 group by year1, property_type;