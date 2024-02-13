# groupBy

---
* `groupBy()` function is used to collect the identical data into groups on DataFrame and perform count, sum, avg, min, max functions on the grouped data.
```python
# create dataframe
simpleData = [("James","Sales","NY",90000,34,10000),
    ("Michael","Sales","NY",86000,56,20000),
    ("Robert","Sales","CA",81000,30,23000),
    ("Maria","Finance","CA",90000,24,23000),
    ("Raman","Finance","CA",99000,40,24000),
    ("Scott","Finance","NY",83000,36,19000),
    ("Jen","Finance","NY",79000,53,15000),
    ("Jeff","Marketing","CA",80000,25,18000),
    ("Kumar","Marketing","NY",91000,50,21000)
  ]

schema = ["employee_name","department","state","salary","age","bonus"]
df = spark.createDataFrame(data=simpleData, schema = schema)
df.printSchema()
df.show(truncate=False)
```
#### Group by on data frame columns
```python
df.groupBy("department").sum("salary").show(truncate=False)
df.groupBy("department").count()
df.groupBy("department").min("salary")
df.groupBy("department").max("salary")
df.groupBy("department").avg( "salary")
df.groupBy("department").mean( "salary") 
```
#### Using multiple columns
```python
#GroupBy on multiple columns
df.groupBy("department","state") \
    .sum("salary","bonus") \
    .show(false)
```
#### Running more aggregates at a time
```python
from pyspark.sql.functions import sum,avg,max
df.groupBy("department") \
    .agg(sum("salary").alias("sum_salary"), \
         avg("salary").alias("avg_salary"), \
         sum("bonus").alias("sum_bonus"), \
         max("bonus").alias("max_bonus") \
     ) \
```
#### Using filter on aggregate data
```python
from pyspark.sql.functions import sum,avg,max
df.groupBy("department") \
    .agg(sum("salary").alias("sum_salary"), \
      avg("salary").alias("avg_salary"), \
      sum("bonus").alias("sum_bonus"), \
      max("bonus").alias("max_bonus")) \
    .where(col("sum_bonus") >= 50000) \
    .show(truncate=False)
```