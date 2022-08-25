from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local") \
    .appName("pokemon_data") \
    .getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("WARN")

Popularity_Trend_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("file:/mnt/c/Users/Benjamin/Desktop/Training/p2project/p2_Team4_Data.csv")

popularity_simple = Popularity_Trend_df.select(["product_name","product_category", "qty", "datetime", "country"])

# pokemon_info = pokemon_df.select(["ID", "Generation", "Legendary"])

popularity_simple.createOrReplaceTempView("popularity_simple")
# pokemon_info.createOrReplaceTempView("pokemon_info")
category_df = spark.sql("SELECT DISTINCT product_name as pn, product_category as pc FROM popularity_simple WHERE product_category !='null' ORDER BY pn")

category_df.createOrReplaceTempView("category_df")

summary_df = spark.sql("SELECT pc, sum(qty) as Sold, IFNULL(DATE_FORMAT(datetime, 'MMM'), SUBSTRING_INDEX(SUBSTRING_INDEX(datetime,',',2),' ',-1)) AS Month, country FROM popularity_simple JOIN category_df ON pn=product_name WHERE qty != -1000 AND pc IN ('history', 'fiction', 'nonfiction') GROUP BY pc, country, Month ORDER BY pc, country, Month")
summary_df.show(13)

summary_df.coalesce(1).write.csv("file:/mnt/c/Users/Benjamin/Desktop/Training/Week6/country_month")

spark.stop()