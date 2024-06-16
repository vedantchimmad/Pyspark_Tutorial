from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]") \
       .appName("SparkByExamples.com") \
       .getOrCreate()

df = spark.read.csv("C:/Users/VEDANT/Pyspark_Tutorial/resource/data/read/peoples.csv")
df.printSchema()
