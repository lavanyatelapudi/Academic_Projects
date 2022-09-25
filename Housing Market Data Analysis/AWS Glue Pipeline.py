import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="s3-db", table_name="all_sales_csv", transformation_ctx="S3bucket_node1"
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[
        ("median_sale_price", "double", "median_sale_price", "double"),
        ("median_list_price", "double", "median_list_price", "double"),
        ("median_list_ppsf", "double", "median_list_ppsf", "double"),
        ("homes_sold", "long", "homes_sold", "long"),
        ("pending_sales", "long", "pending_sales", "long"),
        ("new_listings", "long", "new_listings", "long"),
        ("inventory", "long", "inventory", "long"),
        ("months_of_supply", "double", "months_of_supply", "double"),
        ("median_dom", "long", "median_dom", "long"),
        ("avg_sale_to_list", "double", "avg_sale_to_list", "double"),
        ("sold_above_list", "double", "sold_above_list", "double"),
        ("price_drops", "double", "price_drops", "double"),
        ("off_market_in_two_weeks", "double", "off_market_in_two_weeks", "double"),
        ("region", "string", "region", "string"),
        ("property_type", "string", "property_type", "string"),
        ("state", "string", "state", "string"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node MySQL table
MySQLtable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ApplyMapping_node2,
    database="aws-rds",
    table_name="real_estate_all_sales",
    transformation_ctx="MySQLtable_node3",
)

job.commit()
