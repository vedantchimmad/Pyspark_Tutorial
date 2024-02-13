# Pivote and Unpivote

---
* `pivot()` function is used to rotate/transpose the data from one column into multiple Dataframe columns and back using unpivot(). 
* Pivot() It is an aggregation where one of the grouping columns values is transposed into individual columns with distinct data.
```python
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import expr
#Create spark session
data = [("Banana",1000,"USA"), ("Carrots",1500,"USA"), ("Beans",1600,"USA"), \
("Orange",2000,"USA"),("Orange",2000,"USA"),("Banana",400,"China"), \
("Carrots",1200,"China"),("Beans",1500,"China"),("Orange",4000,"China"), \
("Banana",2000,"Canada"),("Carrots",2000,"Canada"),("Beans",2000,"Mexico")]

columns= ["Product","Amount","Country"]
df = spark.createDataFrame(data = data, schema = columns)
df.printSchema()
df.show(truncate=False)
```
#### Pivote()
```python
pivotDF = df.groupBy("Product").pivot("Country").sum("Amount")
pivotDF.printSchema()
pivotDF.show(truncate=False)
```
#### Unpivote()
```python
from pyspark.sql.functions import expr
unpivotExpr = "stack(3, 'Canada', Canada, 'China', China, 'Mexico', Mexico) as (Country,Total)"
unPivotDF = pivotDF.select("Product", expr(unpivotExpr)) \
.where("Total is not null")
unPivotDF.show(truncate=False)
unPivotDF.show()
```