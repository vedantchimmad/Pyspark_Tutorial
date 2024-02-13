# partitionBy

---
* PySpark partitionBy() is a function of pyspark.sql.DataFrameWriter class 
* class which is used to partition the large dataset (DataFrame) into smaller files based on one or multiple columns while writing to disk
```python
df=spark.read.option("header",True) \
        .csv("/tmp/resources/simple-zipcodes.csv")
df.printSchema()
```
#### partitionBy()
PySpark splits the records based on the partition column and stores each partition data into a sub-directory.
```python
#partitionBy()
df.write.option("header",True) \
        .partitionBy("state") \
        .mode("overwrite") \
        .csv("/tmp/zipcodes-state")
```
####  partitionBy() Multiple Columns
```python
#partitionBy() multiple columns
df.write.option("header",True) \
        .partitionBy("state","city") \
        .mode("overwrite") \
        .csv("/tmp/zipcodes-state")
```
####  repartition() and partitionBy() together
if you wanted to further divide into several partitions, use repartition() and partitionBy() together
```python
#Use repartition() and partitionBy() together
dfRepart.repartition(2)
        .write.option("header",True) \
        .partitionBy("state") \
        .mode("overwrite") \
        .csv("c:/tmp/zipcodes-state-more")
```