# RDD

---
###  RDD(Resilient distributed dataset)
*	RDD (Resilient Distributed Dataset) is a fundamental building block of PySpark which is fault-tolerant, immutable distributed collections of objects.
*	RDD’s can have a name and unique identifier (id)

#### RDD benefits
* **In-Memory Processing** : PySpark loads the data from disk and process in memory and keeps the data in memory
* **Immutability** : RDD’s are immutable in nature meaning, once RDDs are created you cannot modify. When we apply transformations on RDD, PySpark creates a new RDD and maintains the RDD Lineage.
* **Fault Tolerance** : PySpark operates on fault-tolerant data stores on HDFS, S3 e.t.c hence any RDD operation fails, it automatically reloads the data from other partitions.
* **Lazy Evolution** : PySpark does not evaluate the RDD transformations as they appear/encountered, evaluates the all transformation when it sees the first RDD action.
* **Partitioning** : When you create RDD from a data, It by default partitions the elements in a RDD. By default, it partitions to the number of cores available.
#### Creating RDD:
*	Parallelize()
*	Referencing data sets in external storage

**1)	Parallelize**

*	PySpark `parallelize()` is a function in SparkContext and is used to create an RDD from a list collection.
```python
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('parallelize').getOrCreate()
sparkContext=spark.sparkContext
rdd=sparkContext.parallelize([1,2,3,4,5])
rddCollect = rdd.collect()
print("Number of Partitions: "+str(rdd.getNumPartitions()))
print("Action: First element: "+str(rdd.first()))
print(rddCollect)
```
**2)Referencing data sets from external storage**

Reading CSV files in data frame
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder().master("local[1]") \
      .appName("SparkByExamples.com") \
      .getOrCreate()

df = spark.read.csv("/tmp/resources/zipcodes.csv")
df.printSchema()
             or
df = spark.read.format("csv")
.load("/tmp/resources/zipcodes.csv")
            or
df = spark.read.format("org.apache.spark.sql.csv")
.load("/tmp/resources/zipcodes.csv")
df.printSchema()
```
Writing CSV file
```python
df2.write.mode('overwrite').csv("/tmp/spark_output/zipcodes")
     or 
df2.write.format("csv").mode('overwrite').save("/tmp/spark_output/zipcodes")
```
### Repartition and Coalesce
Sometimes we may need to repartition the RDD, 

PySpark provides two ways to repartition
1. first using `repartition()` method which shuffles data from all nodes also called full shuffle 
2. `coalesce()` method which shuffle data from minimum nodes, for examples if you have data in 4 partitions and doing coalesce(2) moves data from just 2 nodes.  
#### RDD operation:
1.    RDD Transformation
2.    RDD action

**1)	RDD Transformation**

Transformations are lazy operations, instead of updating an RDD, these operations return another RDD.
* **Narrow transformation**

Narrow transformations are the result of `map()` and `filter()` functions and these compute data that live on a single partition meaning there will not be any data movement between partitions to execute narrow transformations.
>[!Example:]
> 
>map(), mapPartition(), flatMap(), filter(), union()

* **Wider transformation**

Wider transformations are the result of groupByKey() and reduceByKey() functions and these compute data that live on many partitions meaning there will be data movements between partitions to execute wider transformations.
>[!Example:]
>
>groupByKey(), aggregateByKey(), aggregate(), join(), repartition()

**2)	RDD Action**

return the values from an RDD to a driver program.
>[!Example:]
> 
>Count(),first(),max(),reduce(),take(),collect()

**Types of RDD:**
* PairRDDFunctions or PairRDD 
* ShuffledRDD
* DoubleRDD  
* SequenceFileRDD
* HadoopRDD
* ParallelCollectionRDD

#### Create of empty RDD
**_Create RDD_**

_1.	Create empty RDD using emptyRDD():_
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

#Creates Empty RDD
emptyRDD = spark.sparkContext.emptyRDD()
print(emptyRDD)
```

_2.	Create empty RDD using parallelize()_
```python
 #Creates Empty RDD using parallelize
rdd2= spark.sparkContext.parallelize([])
print(rdd2)
```