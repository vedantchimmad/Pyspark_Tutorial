# UnionByName

---
* to merge/union two DataFrames with column names.
* this function also takes param allowMissingColumns with the value True if you have a different number of columns on two DataFrames.

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

# Create DataFrame df1 with columns name, and id
data = [("James",34), ("Michael",56), \
        ("Robert",30), ("Maria",24) ]

df1 = spark.createDataFrame(data = data, schema=["name","id"])
df1.printSchema()

# Create DataFrame df2 with columns name and id
data2=[(34,"James"),(45,"Maria"), \
       (45,"Jen"),(34,"Jeff")]

df2 = spark.createDataFrame(data = data2, schema = ["id","name"])
df2.printSchema()
```
#### unionByName() with different number of columns
* If you have a different number of columns then use allowMissingColumns=True. When using this, the result of the DataFrmae contains null values for the columns that are missing on the DataFrame.
```python
# Create DataFrames with different column names
df1 = spark.createDataFrame([[5, 2, 6]], ["col0", "col1", "col2"])
df2 = spark.createDataFrame([[6, 7, 3]], ["col1", "col2", "col3"])

# Using allowMissingColumns
df3 = df1.unionByName(df2, allowMissingColumns=True)
df3.printSchema
df3.show()
```
