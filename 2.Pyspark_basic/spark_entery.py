import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Simple").master("local[1]").getOrCreate()

df=spark.read.format("csv").option("header","true").load("C:/Users/VEDANT/Documents/athlete_events.csv")

df.show()