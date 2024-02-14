# JSON

---
* the JSON functions allow you to work with JSON data within DataFrames. 
* These functions help you parse, manipulate, and extract data from JSON columns or strings.

| JSON FUNCTIONS	       | DESCRIPTION                                                            |
|-----------------------|------------------------------------------------------------------------|
| from_json()	          | Converts JSON string into Struct type or Map type.                     |
 | to_json()	            | Converts MapType or Struct type to JSON string.                        |
 | json_tuple()          | 	Extract the Data from JSON and create them as a new columns.          |
 | get_json_object()	    | Extracts JSON element from a JSON string based on json path specified. |
 | schema_of_json()      | 	Create schema string from JSON string                                 |
```python
from pyspark.sql import SparkSession,Row
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

jsonString="""{"Zipcode":704,"ZipCodeType":"STANDARD","City":"PARC PARQUE","State":"PR"}"""
df=spark.createDataFrame([(1, jsonString)],["id","value"])
df.show(truncate=False)
```
####  PySpark JSON Functions
* PySpark from_json() function is used to convert JSON string into Struct type or Map type.
```python
#Convert JSON string column to Map type
from pyspark.sql.types import MapType,StringType
from pyspark.sql.functions import from_json
df2=df.withColumn("value",from_json(df.value,MapType(StringType(),StringType())))
df2.printSchema()
df2.show(truncate=False)
```
#### to_json()
to_json() function is used to convert DataFrame columns MapType or Struct type to JSON string.
```python
from pyspark.sql.functions import to_json,col
df2.withColumn("value",to_json(col("value"))) \
   .show(truncate=False)
```
#### json_tuple()
* Function json_tuple() is used the query or extract the elements from JSON column and create the result as a new columns.
```python
from pyspark.sql.functions import json_tuple
df.select(col("id"),json_tuple(col("value"),"Zipcode","ZipCodeType","City")) \
    .toDF("id","Zipcode","ZipCodeType","City") \
    .show(truncate=False)
```
#### get_json_object()
* get_json_object() is used to extract the JSON string based on path from the JSON column.
```python
from pyspark.sql.functions import get_json_object
df.select(col("id"),get_json_object(col("value"),"$.ZipCodeType").alias("ZipCodeType")) \
    .show(truncate=False)
```
#### schema_of_json()
* Use schema_of_json() to create schema string from JSON string column.
```python
from pyspark.sql.functions import schema_of_json,lit
schemaStr=spark.range(1) \
    .select(schema_of_json(lit("""{"Zipcode":704,"ZipCodeType":"STANDARD","City":"PARC PARQUE","State":"PR"}"""))) \
    .collect()[0][0]
print(schemaStr)
```