#Create Spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .master("local") \
        .appName("product_data") \
            .getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("WARN")

product_file_df = spark.read.option("header", True).option("inferSchema", True).csv("file:/home/nithia_justin/p2_Team4_Data.csv")

#quantity_filter = "qty in ('(random.random()*20 + 1).__round__()')"
quantity_filter = "qty in ('1','2','3','4','5','6','7','8','9','10')"
txn_id_regex = "(?i)[a-z]{2}\-[0-9]{6}"
valid_countries = ['United States', 'Italy', 'Nigeria', 'England', 'Spain', 'France', 'Germany', 'Portugal', 'Japan', 'Mexico']

clean_df = product_file_df.filter(quantity_filter).filter(col("country").isin(valid_countries))

clean_df.createOrReplaceTempView("clean_df")
final_df_0 = spark.sql("select country,count(product_name) as Sales from clean_df group by country order by sales Desc")
#final_df_0 = spark.sql("select country,sum(qty) as Sales from clean_df group by country order by sales Desc")
final_df_0.show(50)

final_df_0.coalesce(1).write.csv("file:/mnt/c/Users/Nithia Justin/Desktop/Revature/Revature Training docs/WEEK_6_CODING/Country_other_team")
spark.stop()