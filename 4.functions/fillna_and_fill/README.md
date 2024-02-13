# Fillna and Fill

---
* DataFrame.`fillna()` or DataFrameNaFunctions.`fill()` is used to replace NULL/None values on all or selected multiple DataFrame columns with either zero(0), empty string, space, or any constant literal values.
>Syntax
> 
>fillna(value, subset=None)
> 
>fill(value, subset=None)
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .master("local[1]") \
    .appName("SparkByExamples.com") \
    .getOrCreate()

filePath="resources/small_zipcode.csv"
df = spark.read.options(header='true', inferSchema='true') \
          .csv(filePath)

df.printSchema()
df.show(truncate=False)
```
#### Replace null/none value with Zero(0)
```python
#Replace 0 for null for all integer columns
df.na.fill(value=0).show()

#Replace 0 for null on only population column 
df.na.fill(value=0,subset=["population"]).show()
#both statements yields the same output, since we have just an integer column population with null values Note that it replaces only Integer columns since our value is 0.
```
#### Replca Null/none value with string
```python
df.na.fill("").show(false)
    Or
df.na.fill("unknown",["city"]) \
    .na.fill("",["type"]).show()
```
