# MapType

---
* PySpark MapType (also called map type) is a data type to represent Python Dictionary (dict) to store key-value pair, 
* PySpark SQL function create_map() is used to convert selected DataFrame columns to MapType,
*  create_map() takes a list of columns you wanted to convert as an argument and returns a MapType column.
```python
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
data = [ ("36636","Finance",3000,"USA"), 
    ("40288","Finance",5000,"IND"), 
    ("42114","Sales",3900,"USA"), 
    ("39192","Marketing",2500,"CAN"), 
    ("34534","Sales",6500,"USA") ]
schema = StructType([
     StructField('id', StringType(), True),
     StructField('dept', StringType(), True),
     StructField('salary', IntegerType(), True),
     StructField('location', StringType(), True)
     ])

df = spark.createDataFrame(data=data,schema=schema)
df.printSchema()
df.show(truncate=False)

from pyspark.sql.functions import col,lit,create_map
df = df.withColumn("propertiesMap",create_map(
    lit("salary"),col("salary"),
    lit("location"),col("location")
)).drop("salary","location")
df.printSchema()
df.show(truncate=False)
```
#### Create MapType From StructType
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


df.withColumn("hair",df.properties.getItem("hair"))
    .withColumn("eye",df.properties.getItem("eye"))
    .drop("properties")
    .show()

df.withColumn("hair",df.properties["hair"])
    .withColumn("eye",df.properties["eye"])
    .drop("properties")
    .show()
```
#### map_keys() – Get All Map Keys
```python
from pyspark.sql.functions import map_keys
df.select(df.name,map_keys(df.properties)).show()
```
#### map_values() – Get All map Values
```python
from pyspark.sql.functions import map_values
df.select(df.name,map_values(df.properties)).show()
```
