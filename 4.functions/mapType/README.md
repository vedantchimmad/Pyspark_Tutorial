# mapType

---
* MapType (also called map type) is a data type to represent Python Dictionary (dict) to store key-value pair, 
* a MapType object comprises three fields, keyType (a DataType), valueType (a DataType) and valueContainsNull (a BooleanType).

#### Create from pysapark
```python
from pyspark.sql.types import StringType, MapType
mapCol = MapType(StringType(),StringType(),False)
```
#### Create mapType from StructType
```python
from pyspark.sql.types import StructField, StructType, StringType, MapType
schema = StructType([
StructField('name', StringType(), True),
StructField('properties', MapType(StringType(),StringType()),True)
])

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

dataDictionary = [
('James',{'hair':'black','eye':'brown'}),
('Michael',{'hair':'brown','eye':None}),
('Robert',{'hair':'red','eye':'black'}),
('Washington',{'hair':'grey','eye':'grey'}),
('Jefferson',{'hair':'brown','eye':''})
]
df = spark.createDataFrame(data=dataDictionary, schema = schema)
df.printSchema()
df.show(truncate=False)
```
#### Access maptype elememnts
```python
df3=df.rdd.map(lambda x: \
(x.name,x.properties["hair"],x.properties["eye"])) \
.toDF(["name","hair","eye"])
df3.printSchema()
df3.show()
```
* use another way to get the value of a key from Map using getItem() of Column type, this method takes a key as an argument and returns a value.
```python
df.withColumn("hair",df.properties.getItem("hair")) \
.withColumn("eye",df.properties.getItem("eye")) \
.drop("properties") \
.show()

df.withColumn("hair",df.properties["hair"]) \
.withColumn("eye",df.properties["eye"]) \
.drop("properties") \
.show()
```
#### Functions
1.	Explode
```python
from pyspark.sql.functions import explode
df.select(df.name,explode(df.properties)).show()
```
2.	Map_keys()
```python
from pyspark.sql.functions import map_keys
df.select(df.name,map_keys(df.properties)).show()
```
3.	Map_values()
```python
from pyspark.sql.functions import map_values
df.select(df.name,map_values(df.properties)).show()
```