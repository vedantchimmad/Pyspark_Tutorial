# months_between

---
months_between() you can calculate the difference between two dates in days, months, and year,
```python
from pyspark.sql.functions import *
data = [("1","2019-07-01"),("2","2019-06-24"),("3","2019-08-24")]
df=spark.createDataFrame(data=data,schema=["id","date"])

df.withColumn("datesDiff", datediff(current_date(),col("date")))
    .withColumn("montsDiff", months_between(current_date(),col("date")))
    .withColumn("montsDiff_round",round(months_between(current_date(),col("date")),2))
    .withColumn("yearsDiff",months_between(current_date(),col("date"))/lit(12))
    .withColumn("yearsDiff_round",round(months_between(current_date(),col("date"))/lit(12),2))
    .show()
```

