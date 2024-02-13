# collect

---
* RDD/DataFrame `collect()` is an action operation that is used to retrieve all the elements of the dataset (from all nodes) to the driver node. 
* We should use the collect() on smaller dataset usually after filter(), group() e.t.c
```python
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

dept = [("Finance",10), \
    ("Marketing",20), \
    ("Sales",30), \
    ("IT",40) \
  ]
deptColumns = ["dept_name","dept_id"]
deptDF = spark.createDataFrame(data=dept, schema = deptColumns)
deptDF.show(truncate=False)

dataCollect = deptDF.collect()
print(dataCollect)
```
* retrieves all elements in a DataFrame as an Array of Row type to the driver node.
```
[Row(dept_name='Finance', dept_id=10), 
Row(dept_name='Marketing', dept_id=20), 
Row(dept_name='Sales', dept_id=30), 
Row(dept_name='IT', dept_id=40)]
```
