# Translate

---
By using translate() string function you can replace character by character of DataFrame column value.
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()
address = [(1,"14851 Jeffrey Rd","DE"),
    (2,"43421 Margarita St","NY"),
    (3,"13111 Siemon Ave","CA")]
df =spark.createDataFrame(address,["id","address","state"])
df.show()

#Using translate to replace character by character
from pyspark.sql.functions import translate
df.withColumn('address', translate('address', '123', 'ABC'))
    .show(truncate=False)
```
