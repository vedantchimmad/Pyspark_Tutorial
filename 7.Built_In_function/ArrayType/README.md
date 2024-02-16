# ArrayType


---
* PySpark ArrayType is a collection data type that extends the DataType class which is a superclass of all types in PySpark.
```python
data = [
 ("James,,Smith",["Java","Scala","C++"],["Spark","Java"],"OH","CA"),
 ("Michael,Rose,",["Spark","Java","C++"],["Spark","Java"],"NY","NJ"),
 ("Robert,,Williams",["CSharp","VB"],["Spark","Python"],"UT","NV")
]

from pyspark.sql.types import StringType, ArrayType,StructType,StructField
schema = StructType([ 
    StructField("name",StringType(),True), 
    StructField("languagesAtSchool",ArrayType(StringType()),True), 
    StructField("languagesAtWork",ArrayType(StringType()),True), 
    StructField("currentState", StringType(), True), 
    StructField("previousState", StringType(), True)
  ])

df = spark.createDataFrame(data=data,schema=schema)
df.printSchema()
df.show()
```
## ArrayType (Array) Functions
### explode()
Use explode() function to create a new row for each element in the given array column.
```python
from pyspark.sql.functions import explode
df.select(df.name,explode(df.languagesAtSchool)).show()
```
### Split()
split() sql function returns an array type after splitting the string column by delimiter.
```python
from pyspark.sql.functions import split
df.select(split(df.name,",").alias("nameAsArray")).show()
```
### array()
Use array() function to create a new array column by merging the data from multiple columns.
```python
from pyspark.sql.functions import array
df.select(df.name,array(df.currentState,df.previousState).alias("States")).show()
```
### array_contains
array_contains() sql function is used to check if array column contains a value.
```python
from pyspark.sql.functions import array_contains
df.select(df.name,array_contains(df.languagesAtSchool,"Java")
    .alias("array_contains")).show()
```
