# datediff

---
* Using PySpark SQL functions datediff(), months_between() you can calculate the difference between two dates in days, months, and year,
```python
from pyspark.sql.functions import *
data = [("1","2019-07-01"),("2","2019-06-24"),("3","2019-08-24")]
df=spark.createDataFrame(data=data,schema=["id","date"])

df.select(
      col("date"),
      current_date().alias("current_date"),
      datediff(current_date(),col("date")).alias("datediff")
    ).show()
```
