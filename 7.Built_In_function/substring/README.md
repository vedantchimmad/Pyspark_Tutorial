# substring

---
* the `substring()` function is used to extract the substring from a DataFrame string column by providing the position and length of the string
>Syntax
>
>substring(str, pos, len)
```python
# Imports
import pyspark
from pyspark.sql import SparkSession 
from pyspark.sql.functions import col, substring
spark=SparkSession.builder.appName("stringoperations").getOrCreate()
# Create Sample Data
data = [(1,"20200828"),(2,"20180525")]
columns=["id","date"]
df=spark.createDataFrame(data,columns)
df.withColumn('year', substring('date', 1,4))\
    .withColumn('month', substring('date', 5,2))\
    .withColumn('day', substring('date', 7,2))
df.printSchema()
df.show(truncate=False)
```
#### Using substring() with select()
```python
# substring() with select()
df.select('date', substring('date', 1,4).alias('year'), \
                  substring('date', 5,2).alias('month'), \
                  substring('date', 7,2).alias('day'))  
```
#### Using substring() with selectExpr()
Sample example using selectExpr to get a substring of column(date) as year, month, day.
```python
# substring() with selectExpr()
df.selectExpr('date', 'substring(date, 1,4) as year', \
                  'substring(date, 5,2) as month', \
                 'substring(date, 7,2) as day')
```
#### Using substr() from Column type
```python
df3=df.withColumn('year', col('date').substr(1, 4))\
  .withColumn('month',col('date').substr(5, 2))\
  .withColumn('day', col('date').substr(7, 2))
```
