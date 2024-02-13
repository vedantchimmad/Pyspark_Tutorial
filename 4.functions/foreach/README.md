# Foreach

---
* PySpark foreach() is an action operation that is available in RDD, DataFram to iterate/loop over each element in the DataFrmae,
* This is different than other actions as foreach() function doesn’t return a value instead it executes the input function on each element of an RDD, DataFrame
```python

# Import
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com') \
                    .getOrCreate()

# Prepare Data
columns = ["Seqno","Name"]
data = [("1", "john jones"),
    ("2", "tracey smith"),
    ("3", "amy sanders")]

# Create DataFrame
df = spark.createDataFrame(data=data,schema=columns)
df.show()

# foreach() Example
def f(df):
    print(df.Seqno)
df.foreach(f)
```
