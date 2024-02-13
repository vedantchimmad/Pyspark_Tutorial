# User defined function

---
* you create a function in a Python syntax and wrap it with PySpark SQL udf() or register it as udf and use it on DataFrame and SQL respectively.
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
#### Create python function
```python
def convertCase(str):
    resStr=""
    arr = str.split(" ")
    for x in arr:
       resStr= resStr + x[0:1].upper() + x[1:len(x)] + " "
    return resStr 
```
#### Convert function to UDF
```python
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType

# Converting function to UDF 
convertUDF = udf(lambda z: convertCase(z),StringType())
```
### UDF in select()
```python
df.select(col("Seqno"), \
    convertUDF(col("Name")).alias("Name") ) \
   .show(truncate=False)
```
#### UDF in withColumn()
```python
def upperCase(str):
    return str.upper()


upperCaseUDF = udf(lambda z:upperCase(z),StringType())   

df.withColumn("Cureated Name", upperCaseUDF(col("Name"))) \
  .show(truncate=False)
```
#### Create UDF using annotation
* you can avoid these two steps and create it with just a single step by using annotations.
```python
@udf(returnType=StringType()) 
def upperCase(str):
    return str.upper()

df.withColumn("Cureated Name", upperCase(col("Name"))) \
.show(truncate=False)
```

