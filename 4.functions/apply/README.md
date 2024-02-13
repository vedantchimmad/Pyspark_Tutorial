# Apply

---
* By using withColumn(), sql(), select() you can apply a built-in function or custom function to a column.
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
columns = ["Seqno","Name"]
data = [("1", "john jones"),
    ("2", "tracey smith"),
    ("3", "amy sanders")]

df = spark.createDataFrame(data=data,schema=columns)

df.show(truncate=False)
```
#### Apply function using withColumn()
```python

# Apply function using withColumn
from pyspark.sql.functions import upper
df.withColumn("Upper_Name", upper(df.Name)) \
  .show()
```
#### Apply function using select()
```python
# Apply function using select  
df.select("Seqno","Name", upper(df.Name)) \
  .show()
```