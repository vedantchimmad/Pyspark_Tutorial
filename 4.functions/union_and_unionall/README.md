# Union and union all

---
* PySpark `union()` and `unionAll()` transformations are used to merge two or more DataFrame’s of the same schema or structure.
* Dataframe `union()` – union() method of the DataFrame is used to merge two DataFrame’s of the same structure/schema. If schemas are not the same it returns an error.
* DataFrame `unionAll()` – unionAll() is deprecated since Spark “2.0.0” version and replaced with union().
>[!Note]:
> 
>In other SQL languages, Union eliminates the duplicates but UnionAll merges two datasets including duplicate records.
```python
#First DataFrame

import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

simpleData = [("James","Sales","NY",90000,34,10000), \
    ("Michael","Sales","NY",86000,56,20000), \
    ("Robert","Sales","CA",81000,30,23000), \
    ("Maria","Finance","CA",90000,24,23000) \
  ]

columns= ["employee_name","department","state","salary","age","bonus"]
df = spark.createDataFrame(data = simpleData, schema = columns)
df.printSchema()
df.show(truncate=False)

#Second DataFrame
simpleData2 = [("James","Sales","NY",90000,34,10000), \
    ("Maria","Finance","CA",90000,24,23000), \
    ("Jen","Finance","NY",79000,53,15000), \
    ("Jeff","Marketing","CA",80000,25,18000), \
    ("Kumar","Marketing","NY",91000,50,21000) \
  ]
columns2= ["employee_name","department","state","salary","age","bonus"]

df2 = spark.createDataFrame(data = simpleData2, schema = columns2)

df2.printSchema()
df2.show(truncate=False)
```
### union()
* DataFrame union() method merges two DataFrames and returns the new DataFrame with all rows from two Dataframes regardless of duplicate data.
```python
unionDF = df.union(df2)
unionDF.show(truncate=False)
```
### Merge without duplicate
```python
disDF = df.union(df2).distinct()
disDF.show(truncate=False)
```