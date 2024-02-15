# explode

---
* How to explode & flatten nested array (Array of Array) DataFrame columns into rows using PySpark.
* PySpark explode function can be used to explode an Array of Array (nested Array) ArrayType(ArrayType(StringType)) columns to rows on PySpark DataFrame using python
```python
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('pyspark-by-examples').getOrCreate()

arrayArrayData = [
  ("James",[["Java","Scala","C++"],["Spark","Java"]]),
  ("Michael",[["Spark","Java","C++"],["Spark","Java"]]),
  ("Robert",[["CSharp","VB"],["Spark","Python"]])
]

df = spark.createDataFrame(data=arrayArrayData, schema = ['name','subjects'])
df.printSchema()
df.show(truncate=False)

df.select(df.name,explode(df.subjects)).show(truncate=False)
```
# Flatten
```python
from pyspark.sql.functions import flatten
df.select(df.name,flatten(df.subjects)).show(truncate=False)
```