# Lit

---
unctions `lit()` and `typedLit()` are used to add a new column to DataFrame by assigning a literal or constant value.
```python
# Imports
# prepare sample Data
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
data = [("111",50000),("222",60000),("333",40000)]
columns= ["EmpId","Salary"]
df = spark.createDataFrame(data = data, schema = columns)
```
#### Simple usage of lit() function
```python
# Usage of lit() 
from pyspark.sql.functions import col,lit
df2 = df.select(col("EmpId"),col("Salary"),lit("1").alias("lit_value1"))
df2.show(truncate=False)
```
#### lit() function with withColumn
```python
# Usage of lit() with withColumn()
from pyspark.sql.functions import when, lit, col
df3 = df2.withColumn("lit_value2", when((col("Salary") >=40000) & (col("Salary") <= 50000),lit("100")).otherwise(lit("200")))
df3.show(truncate=False)
```
#### typedLit() Function
Difference between lit() and typedLit() is that the typedLit() function can handle collection types e.g.: Array, Dictionary(map), etc.
```python
# Usage of typedlit() 
df4 = df4.withColumn("lit_value3", typedLit("flag", StringType()))
df4.show(truncate=False)
```
