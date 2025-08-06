# Pyspark Basic 

---
PySpark is the Python API for Apache Spark, an open-source, distributed computing system that enables fast processing of large-scale data. PySpark allows Python developers to interface with Spark and harness the power of distributed computing for big data analytics.

---

### 📌 Key Features of PySpark

| Feature                      | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| Distributed Computing       | Executes operations in parallel across multiple nodes.                     |
| Fault Tolerance             | Automatically recovers lost computations using RDD lineage.                |
| Lazy Evaluation             | Transformations are not executed until an action is triggered.             |
| In-Memory Computation       | Caches intermediate data in memory to improve performance.                 |
| Language Support            | Supports Python, Scala, Java, and R.                                       |
| Integration                 | Works with Hadoop, Hive, HDFS, JDBC, Cassandra, AWS S3, etc.               |

---

### 🧱 PySpark Components

| Component    | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| SparkContext | Main entry point for Spark functionality.                                   |
| RDD          | Resilient Distributed Dataset; fundamental data structure in Spark.         |
| DataFrame    | Distributed collection of data organized into named columns.                |
| SQLContext   | Enables execution of SQL queries.                                           |
| SparkSession | Unified entry point for reading data, SQL, streaming, MLlib, etc.          |

---

### ⚙️ PySpark Architecture

```plaintext
                +----------------------------+
                |        Driver Program      |
                |----------------------------|
                | SparkContext               |
                | - Task Scheduler           |
                | - DAGScheduler             |
                | - BackendScheduler         |
                +------------|---------------+
                             |
                             v
+----------------+     +------------+     +----------------+
| Executor (Node) | --> | Executor   | --> | Executor       |
| - Task          |     | - Task     |     | - Task         |
| - Storage       |     | - Storage  |     | - Storage      |
+----------------+     +------------+     +----------------+

Cluster Manager (e.g., YARN, Mesos, Standalone, Kubernetes)
```
### 🔄 PySpark Workflow
```python
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder
    .appName("PySparkExample")
    .getOrCreate()

# Load data into DataFrame
df = spark.read.csv("data.csv", header=True, inferSchema=True)

# Perform transformation
df_filtered = df.filter(df["age"] > 25)

# Action to trigger computation
df_filtered.show()
```
---
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


