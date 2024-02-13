# withColumn

---
* `withColumn()` is a transformation function of DataFrame which is used to change the value, convert the datatype of an existing column, create a new column, 

```python
# Creating dataframe
data = [('James','','Smith','1991-04-01','M',3000),
  ('Michael','Rose','','2000-05-19','M',4000),
  ('Robert','','Williams','1978-09-05','M',4000),
  ('Maria','Anne','Jones','1967-12-01','F',4000),
  ('Jen','Mary','Brown','1980-02-17','F',-1)
]

columns = ["firstname","middlename","lastname","dob","gender","salary"]
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
df = spark.createDataFrame(data=data, schema = columns)
```
#### change data type using cast()
```python
df.withColumn("salary",col("salary").cast("Integer")).show()
```
### update the value of existing column
```python
df.withColumn("salary",col("salary")*100).show()
```
#### create the new column form existing 
```python
df.withColumn("CopiedColumn",col("salary")* -1).show()
```
