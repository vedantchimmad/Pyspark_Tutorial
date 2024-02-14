# When Otherwise

---
**When Otherwise** – `when()` is a SQL function that returns a Column type and `otherwise()` is a function of Column, if otherwise() is not used, it returns a None/NULL value.
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
data = [("James","M",60000),("Michael","M",70000),
        ("Robert",None,400000),("Maria","F",500000),
        ("Jen","",None)]

columns = ["name","gender","salary"]
df = spark.createDataFrame(data = data, schema = columns)
df.show()
```
#### when() otherwise() 
```python
from pyspark.sql.functions import when
df2 = df.withColumn("new_gender", when(df.gender == "M","Male")
                                 .when(df.gender == "F","Female")
                                 .when(df.gender.isNull() ,"")
                                 .otherwise(df.gender))
df2.show()
```
OR
```python
# Using Select
df2=df.select(col("*"),when(df.gender == "M","Male")
                  .when(df.gender == "F","Female")
                  .when(df.gender.isNull() ,"")
                  .otherwise(df.gender).alias("new_gender"))
```
#### Multiple Conditions using & and | operator
using PySpark When Otherwise with multiple conditions by using and (&) or (|) operators.
```python

df5.withColumn(“new_column”, when((col(“code”) == “a”) | (col(“code”) == “d”), “A”)
.when((col(“code”) == “b”) & (col(“amt”) == “4”), “B”)
.otherwise(“A1”)).show()
```
