# to_date

---
* PySpark functions provide to_date() function to convert timestamp to date (DateType),
* Date (DateType) format would be yyyy-MM-dd.
```python
df=spark.createDataFrame(
        data = [ ("1","2019-06-24 12:01:19.000")],
        schema=["id","input_timestamp"])
df.printSchema()
```
#### Using to_date() – Convert Timestamp String to Date
```python
from pyspark.sql.functions import *

#Timestamp String to DateType
df.withColumn("date_type",to_date("input_timestamp")) \
  .show(truncate=False)

#Timestamp Type to DateType
df.withColumn("date_type",to_date(current_timestamp())) \
  .show(truncate=False) 
```
#### Using Column cast() Function
```python
# Using Cast to convert Timestamp String to DateType
df.withColumn('date_type', col('input_timestamp').cast('date')) \
       .show(truncate=False)

# Using Cast to convert TimestampType to DateType
df.withColumn('date_type', to_timestamp('input_timestamp').cast('date')) \
  .show(truncate=False)
```
