# Window

---
* PySpark Window functions are used to calculate results, such as the rank, row number, etc., over a range of input rows.
* PySpark Window functions operate on a group of rows (like frame, partition) and return a single value for every input row.
```python
# Create SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

simpleData = (("James", "Sales", 3000), \
    ("Michael", "Sales", 4600),  \
    ("Robert", "Sales", 4100),   \
    ("Maria", "Finance", 3000),  \
    ("James", "Sales", 3000),    \
    ("Scott", "Finance", 3300),  \
    ("Jen", "Finance", 3900),    \
    ("Jeff", "Marketing", 3000), \
    ("Kumar", "Marketing", 2000),\
    ("Saif", "Sales", 4100) \
  )
 
columns= ["employee_name", "department", "salary"]
df = spark.createDataFrame(data = simpleData, schema = columns)
df.printSchema()
df.show(truncate=False)
```
## Window Ranking functions
* like `row_number()`, `rank()`, and `dense_rank()`, assign sequential numbers to DataFrame rows based on specified criteria within defined partitions.
* The `row_number()` assigns unique sequential numbers, 
* `rank()` provides the ranking with gaps, 
* `dense_rank()` offers ranking without gaps.
#### row_number Window Function
* row_number() window function gives the sequential row number starting from 1 to the result of each window partition.
```python
# row_number() example
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number
windowSpec  = Window.partitionBy("department").orderBy("salary")

df.withColumn("row_number",row_number().over(windowSpec)) \
    .show(truncate=False)
```
#### rank Window Function
* rank() window function provides a rank to the result within a window partition. 
* This function leaves gaps in rank when there are ties.
```python
# rank() example
from pyspark.sql.functions import rank
df.withColumn("rank",rank().over(windowSpec)) \
    .show()
```
#### dense_rank Window Function
* dense_rank() window function is used to get the result with rank of rows within a window partition without any gaps.
```python
# dense_rank() example 
from pyspark.sql.functions import dense_rank
df.withColumn("dense_rank",dense_rank().over(windowSpec)) \
    .show()
```
#### percent_rank Window Function
```python
# percent_rank() Example
from pyspark.sql.functions import percent_rank
df.withColumn("percent_rank",percent_rank().over(windowSpec)) \
    .show()
```
#### ntile Window Function
* ntile() window function returns the relative rank of result rows within a window partition.
```python
#ntile() Example
from pyspark.sql.functions import ntile
df.withColumn("ntile",ntile(2).over(windowSpec)) \
    .show()
```
## Window Analytic Functions
#### cume_dist Window Function
* This function computes the cumulative distribution of a value within a window partition.
```python
# cume_dist() Example
from pyspark.sql.functions import cume_dist    
df.withColumn("cume_dist",cume_dist().over(windowSpec)) \
   .show()
```
#### lag Window Function
* The lag() function allows you to access a previous row’s value within the partition based on a specified offset.
```python
# lag() Example
from pyspark.sql.functions import lag    
df.withColumn("lag",lag("salary",2).over(windowSpec)) \
      .show()
```
#### lead Window Function
* the lead() function retrieves the column value from the following row within the partition based on a specified offset.
```python

# lead() Example
from pyspark.sql.functions import lead    
df.withColumn("lead",lead("salary",2).over(windowSpec)) \
    .show()
```
## Window Aggregate Functions
*  window aggregate functions, such as sum(), avg(), and min(), compute aggregated values within specified window partitions.
```python
# Aggregate functions examples
windowSpecAgg  = Window.partitionBy("department")
from pyspark.sql.functions import col,avg,sum,min,max,row_number 
df.withColumn("row",row_number().over(windowSpec)) \
  .withColumn("avg", avg(col("salary")).over(windowSpecAgg)) \
  .withColumn("sum", sum(col("salary")).over(windowSpecAgg)) \
  .withColumn("min", min(col("salary")).over(windowSpecAgg)) \
  .withColumn("max", max(col("salary")).over(windowSpecAgg)) \
  .where(col("row")==1).select("department","avg","sum","min","max") \
  .show()
```
