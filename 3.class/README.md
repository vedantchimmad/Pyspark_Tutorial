# StructType,StructField and Column

---
* PySpark StructType & StructField classes are used to programmatically specify the schema to the DataFrame 
* create complex columns like nested struct, array, and map columns. 
* StructType is a collection of StructField’s that defines column name, column data type

```python
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType

spark = SparkSession.builder.master("local[1]") \
.appName('SparkByExamples.com') \
.getOrCreate()

data = [("James","","Smith","36636","M",3000),
("Michael","Rose","","40288","M",4000),
("Robert","","Williams","42114","M",4000),
("Maria","Anne","Jones","39192","F",4000),
("Jen","Mary","Brown","","F",-1)
]

schema = StructType([ \
StructField("firstname",StringType(),True), \
StructField("middlename",StringType(),True), \
StructField("lastname",StringType(),True), \
StructField("id", StringType(), True), \
StructField("gender", StringType(), True), \
StructField("salary", IntegerType(), True) \
])

df = spark.createDataFrame(data=data,schema=schema)
df.printSchema()
df.show(truncate=False)
```
* Adding and changing the struct of the dataframe

Using PySpark SQL function struct(), we can change the struct of the existing DataFrame and add a new StructType to it.
```python
from pyspark.sql.functions import col,struct,when
updatedDF = df2.withColumn("OtherInfo",
struct(col("id").alias("identifier"),
col("gender").alias("gender"),
col("salary").alias("salary"),
when(col("salary").cast(IntegerType()) < 2000,"Low")
.when(col("salary").cast(IntegerType()) < 4000,"Medium")
.otherwise("High").alias("Salary_Grade")
)).drop("id","gender","salary")

updatedDF.printSchema()
updatedDF.show(truncate=False)
```

# Column class
* `pyspark.sql.Column` class provides several functions to work with DataFrame to manipulate the Column values, 
* evaluate the boolean expression to filter rows, retrieve a value or part of a value from a DataFrame column, and to work with list, map & struct columns.
* **Create column class object using lit()**
```python
from pyspark.sql.functions import lit
colObj = lit("sparkbyexamples.com")
```
* **Access column from data frame**
```python
data=[("James",23),("Ann",40)]
df=spark.createDataFrame(data).toDF("name.fname","gender")
df.printSchema()
#root
# |-- name.fname: string (nullable = true)
# |-- gender: long (nullable = true)

# Using DataFrame object (df)
df.select(df.gender).show()
df.select(df["gender"]).show()

#Accessing column name with dot (with backticks)
df.select(df["`name.fname`"]).show()

#Using SQL col() function
from pyspark.sql.functions import col
df.select(col("gender")).show()

#Accessing column name with dot (with backticks)
df.select(col("`name.fname`")).show()
```
* **Column  operator**
```python
data=[(100,2,1),(200,3,4),(300,4,4)]
df=spark.createDataFrame(data).toDF("col1","col2","col3")

#Arthmetic operations
df.select(df.col1 + df.col2).show()
df.select(df.col1 - df.col2).show()
df.select(df.col1 * df.col2).show()
df.select(df.col1 / df.col2).show()
df.select(df.col1 % df.col2).show()

df.select(df.col2 > df.col3).show()
df.select(df.col2 < df.col3).show()
df.select(df.col2 == df.col3).show()
```