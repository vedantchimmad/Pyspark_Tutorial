# Pyspark Basic 

---
### What is PySpark?
*	PySpark is a Spark library written in Python to run Python applications using Apache Spark
*	PySpark is a Python API for Apache Spark.
>[!Note]
>Py4J is a Java library that is integrated within PySpark and allows python to dynamically interface with JVM objects.

### Features
*	In-memory computation
*	Distributed processing using parallelize
*	Can be used with many cluster managers (Spark, Yarn, Mesos e.t.c)
*	Fault-tolerant
*	Immutable
*	Lazy evaluation
*	Cache & persistence
*	Inbuild-optimization when using DataFrames
*	Supports ANSI SQL
### Advantages
*	PySpark is a general-purpose, in-memory, distributed processing engine that allows you to process data efficiently in a distributed fashion.
*	Applications running on PySpark are 100x faster than traditional systems.
*	You will get great benefits using PySpark for data ingestion pipelines.
*	Using PySpark we can process data from Hadoop HDFS, AWS S3, and many file systems.
*	PySpark also is used to process real-time data using Streaming and Kafka.
*	PySpark natively has machine learning and graph libraries.
### What is SparkSession
	It is an entry point to underlying PySpark functionality in order to programmatically create PySpark RDD, DataFrame.

*	You should also know that SparkSession internally creates SparkConfig and SparkContext with the configuration provided with SparkSession.
*	You can create as many SparkSession as you want in a PySpark application using either `SparkSession.builder()` or `SparkSession.newSession()`

#### Create SparkSesstion:
In order to create SparkSession programmatically (in .py file) in PySpark, you need to use the builder pattern method builder() as explained below. getOrCreate() method returns an already existing SparkSession; if not exists, it creates a new SparkSession.

```python
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]") \
.appName('Spark session') \
.getOrCreate()
```
Spark config:
```python
spark = SparkSession.builder \
.master("local[1]") \
.appName("Spark session") \
.config("spark.some.config.option", "config-value") \
.getOrCreate()
```
`master()` – If you are running it on the cluster you need to use your master name as an argument to master(). 
*	Use `local[x]` when running in Standalone mode. x should be an integer value and should be greater than 0
*   this represents how many partitions it should create when using RDD, DataFrame, and Dataset. Ideally

`appName()` – Used to set your application name.

`getOrCreate()` – This returns a SparkSession object if already exists, and creates a new one if not exist.

### SparkContext:
* **pyspark.SparkContext** is an entry point to the PySpark functionality that is used to communicate with the cluster and to create an RDD, accumulator, and broadcast variables.
>[!Note]
>you can create only `one SparkContext per JVM`, in order to create another first you need to stop the existing one using `stop()` method.


