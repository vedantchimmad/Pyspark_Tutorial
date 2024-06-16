import pyspark

from pyspark.sql import SparkSession

spark=SparkSession.builder.master("local[1]").appName("parallelize").getOrCreate()

sparkcontext=spark.sparkContext.parallelize([1,2,3,5,6])

print(sparkcontext.collect())