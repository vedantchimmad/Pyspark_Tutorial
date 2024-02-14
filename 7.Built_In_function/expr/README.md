# Expr

---
* `expr()` function takes SQL expression as a string argument, executes the expression, and returns a PySpark Column type.
#### Concatenate Columns using || (similar to SQL)
using || to concatenate values from two string columns, you can use expr() expression to do exactly same.
```python
#Concatenate columns using || (sql like)
data=[("James","Bond"),("Scott","Varsa")] 
df=spark.createDataFrame(data).toDF("col1","col2") 
df.withColumn("Name",expr(" col1 ||','|| col2")).show()
```
#### Using SQL CASE WHEN with expr()
```python
from pyspark.sql.functions import expr
data = [("James","M"),("Michael","F"),("Jen","")]
columns = ["name","gender"]
df = spark.createDataFrame(data = data, schema = columns)

#Using CASE WHEN similar to SQL.
from pyspark.sql.functions import expr
df2=df.withColumn("gender", expr("CASE WHEN gender = 'M' THEN 'Male' " +
           "WHEN gender = 'F' THEN 'Female' ELSE 'unknown' END"))
df2.show()
```
#### Using an Existing Column Value for Expression
```python
from pyspark.sql.functions import expr
data=[("2019-01-23",1),("2019-06-24",2),("2019-09-20",3)] 
df=spark.createDataFrame(data).toDF("date","increment") 

#Add Month value from another column
df.select(df.date,df.increment,
     expr("add_months(date,increment)")
  .alias("inc_date")).show()
```
>[!Note]
> 
>that Importing SQL functions are not required when using them with expr(). You see above add_months() is used without importing.
#### Giving Column Alias along with expr()
```python
from pyspark.sql.functions import expr
df.select(df.date,df.increment,
     expr("""add_months(date,increment) as inc_date""")
  ).show()
```
#### cast Function with expr()
```python
# Using Cast() Function
df.select("increment",expr("cast(increment as string) as str_increment")) \
  .printSchema()
```
#### Arithmetic operations
```python
# Arthemetic operations
df.select(df.date,df.increment,
     expr("increment + 5 as new_increment")
  ).show()
```
#### Using Filter with expr()
```python
#Use expr()  to filter the rows
from pyspark.sql.functions import expr
data=[(100,2),(200,3000),(500,500)] 
df=spark.createDataFrame(data).toDF("col1","col2") 
df.filter(expr("col1 == col2")).show()
```
