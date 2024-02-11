# Dataframe

---
* DataFrame is a distributed collection of data organized into named columns. 
* It is conceptually equivalent to a table in a relational database
### Creation of data frame:
1.	Using create data frame function
2.	By reading external files


1. #### Using create dataframe
By using `createDataFrame()` function of the SparkSession you can create a DataFrame.
```python
data = [('James','','Smith','1991-04-01','M',3000),
('Michael','Rose','','2000-05-19','M',4000),
('Robert','','Williams','1978-09-05','M',4000),
('Maria','Anne','Jones','1967-12-01','F',4000),
('Jen','Mary','Brown','1980-02-17','F',-1)
]

columns = ["firstname","middlename","lastname","dob","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)
df.show()
```
* 1. **Create dataframe using schema**
```python
#Create Schema
from pyspark.sql.types import StructType,StructField, StringType
schema = StructType([
  StructField('firstname', StringType(), True),
  StructField('middlename', StringType(), True),
  StructField('lastname', StringType(), True)
])

#Create empty DataFrame from empty RDD
df = spark.createDataFrame(emptyRDD,schema)
df.printSchema()
``` 
* 2.	**Convert empty RDD to dataframe**
```python
 #Convert empty RDD to Dataframe
df1 = emptyRDD.toDF(schema)
df1.printSchema()
```
* 3.	**Create empty dataframe using schema**
```python
#Create empty DataFrame directly.
df2 = spark.createDataFrame([], schema)
df2.printSchema()
```
* 4.	**Create empty schema without schema**
```python
#Create empty DatFrame with no schema (no columns)
df3 = spark.createDataFrame([], StructType([]))
df3.printSchema()
```
#### By reading external files
DataFrames are created from external sources like files from the local system, HDFS, S3 Azure, HBase, MySQL table e.t.c.
```python
df = spark.read.csv("/tmp/resources/zipcodes.csv")
df.printSchema()
 
```
