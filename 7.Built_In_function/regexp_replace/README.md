# regexp_replace

---
PySpark SQL function regexp_replace() you can replace a column value with a string for another string/substring.
```python

# Imports
# Create sample Data
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()
address = [(1,"14851 Jeffrey Rd","DE"),
    (2,"43421 Margarita St","NY"),
    (3,"13111 Siemon Ave","CA")]
df =spark.createDataFrame(address,["id","address","state"])
df.show()

#Replace part of string with another string
from pyspark.sql.functions import regexp_replace
df.withColumn('address', regexp_replace('address', 'Rd', 'Road'))
    .show(truncate=False)
```
####  Replace Column Values Conditionally
```python
#Replace string column value conditionally
from pyspark.sql.functions import when
df.withColumn('address', 
    when(df.address.endswith('Rd'),regexp_replace(df.address,'Rd','Road')) \
   .when(df.address.endswith('St'),regexp_replace(df.address,'St','Street')) \
   .when(df.address.endswith('Ave'),regexp_replace(df.address,'Ave','Avenue')) \
   .otherwise(df.address)) \
   .show(truncate=False)
```
