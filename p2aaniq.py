from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import col, substring
import datetime
import re


csv_file = "file:/users/aaniqsalam/p2_Team4_Data.csv"

spark = SparkSession.builder\
    .master("local")\
    .appName("topSellingItems")\
    .getOrCreate()
    

sc = spark.sparkContext
sc.setLogLevel("WARN")



item_df = spark.read.option("header", True).option("InfrSchema", True).csv(csv_file).cache() 



item_category = item_df.select(["country", "datetime", "qty"])


item_category = item_category.withColumn("year", substring("datetime", 1, 10)).withColumn("hour", substring("datetime", 11, 12))
item_category = item_category.withColumn("hr", substring("hour", 1, 3)).withColumn("second", substring("datetime", 4, 8))

item_category = item_category.drop("year")
item_category = item_category.drop("hour")
item_category = item_category.drop("second")



item_category.createOrReplaceTempView("sales")




traffic_selling = spark.sql("SELECT DISTINCT  hr, SUM(qty) AS total FROM  sales  WHERE qty > 0  AND  left(datetime, 1 ) = 2 GROUP BY  hr ORDER BY  total DESC ")
traffic_selling.show()

print("THE HIGHEST SALES TRAFFIC PER COUNTRY")
date_selling = spark.sql("SELECT DISTINCT country, hr, SUM(qty) AS high FROM  sales  WHERE qty > 0   AND  left(datetime, 1 ) = 2 GROUP BY  country, hr ORDER BY country, high DESC")
date_selling.show()


traffic_selling.repartition(1).write.csv("p2_Team4_Output_Data_p2_traffic.csv")
date_selling.repartition(1).write.csv("p2_Team4_Output_Data_p2_date.csv")
spark.stop()
