
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import functions as F
import re

# File path
csv_file = "file:/users/mengistudesta/Documents/p2_Team4_Data.csv"

spark = SparkSession.builder\
    .master("local")\
    .appName("topSellingItems")\
    .getOrCreate()
    

sc = spark.sparkContext
sc.setLogLevel("WARN")
item_df = spark.read.option("header", True).option("InfrSchema", True).csv(csv_file).cache() 

product_info = item_df.select(["product_category", "country", "qty"])

product_info.createOrReplaceTempView("product")

# Changing a string to integer 
# StructField('qty', StringType(), nullable=True),
# item_df.withColumn('qty', item_df['qty'].cast("int"))

# What is the top selling category of items? Per country?
    
print("================================= top selling product category =================================================")

top_selling_product_category = spark.sql("SELECT  DISTINCT product_category, SUM(qty) AS total FROM  product  WHERE qty > 0 AND product_category IS NOT NULL AND product_category IS NOT NULL GROUP BY  product_category ORDER BY total DESC ")
top_selling_product_category.show()

print("===================================== top selling product category per country ==================================")

top_selling_product_category_per_country = spark.sql("SELECT  DISTINCT product_category,  country, SUM(qty) AS total FROM  product  WHERE qty > 0 AND country IS NOT NULL AND product_category IS NOT NULL GROUP BY country, product_category ORDER BY country, total DESC ")
top_selling_product_category_per_country.show()

print("  ++++ SORTED +++++")
sorted = top_selling_product_category_per_country.sort( F.desc("total")).show()



top_selling_product_category_per_country.repartition(1).write.csv("p2_Team4_Output_Data_ctry.csv")
top_selling_product_category.repartition(1).write.csv("p2_Team4_Output_Data_cat.csv")

spark.stop()



