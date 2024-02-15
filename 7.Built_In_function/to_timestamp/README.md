# To_timestamp

---
* Use to_timestamp() function to convert String to Timestamp (TimestampType) in PySpark. 
* The converted time would be in a default format of MM-dd-yyyy HH:mm:ss.SSS
```python

from pyspark.sql.functions import *

df=spark.createDataFrame(
        data = [ ("1","2019-06-24 12:01:19.000")],
        schema=["id","input_timestamp"])
df.printSchema()

#Timestamp String to DateType
df.withColumn("timestamp",to_timestamp("input_timestamp")) \
  .show(truncate=False)

# Using Cast to convert TimestampType to DateType
df.withColumn('timestamp_string', \
         to_timestamp('timestamp').cast('string')) \
  .show(truncate=False)
```
#### Custom string format to Timestamp type
```python
#when dates are not in Spark TimestampType format 'yyyy-MM-dd  HH:mm:ss.SSS'.
#Note that when dates are not in Spark Tiemstamp format, all Spark functions returns null
#Hence, first convert the input dates to Spark DateType using to_timestamp function
df.select(to_timestamp(lit('06-24-2019 12:01:19.000'),'MM-dd-yyyy HH:mm:ss.SSSS')) \
  .show()
```
