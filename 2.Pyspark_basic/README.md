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

## 🔹 SparkSession in PySpark

### 📘 What is `SparkSession`?

`SparkSession` is the **entry point** to programming with Spark using the **DataFrame** and **Dataset** API.  
* It replaces the older `SQLContext` and `HiveContext` from previous Spark versions (before 2.0).

---

### 🧠 Purpose of `SparkSession`

- Provides a unified interface for:
  - Reading and writing data
  - Configuring Spark
  - Working with SQL, DataFrames, Datasets, Streaming, and Machine Learning APIs
- Acts as the **starting point** for all Spark functionality in PySpark applications

---

### 🔧 Syntax

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("YourAppName") \
    .getOrCreate()
````

| Method           | Description                                     |
| ---------------- | ----------------------------------------------- |
| `.builder`       | Entry point to configure the session            |
| `.appName()`     | Assigns a name to your Spark application        |
| `.getOrCreate()` | Creates a new session or reuses an existing one |

---

### 📥 Example: Create SparkSession and Load Data

```python
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
    .appName("ExampleSparkSession") \
    .getOrCreate()

# Load a CSV file into a DataFrame
df = spark.read.csv("employees.csv", header=True, inferSchema=True)

# Display the schema
df.printSchema()

# Show top rows
df.show()
```

---

### 🔍 Common Methods from SparkSession

| Method       | Purpose                                                         |
| ------------ | --------------------------------------------------------------- |
| `read`       | Access DataFrameReader to read files (CSV, JSON, Parquet, etc.) |
| `readStream` | Read streaming data                                             |
| `sql()`      | Run SQL queries directly on DataFrames                          |
| `catalog`    | Interact with metastore (tables, databases)                     |
| `stop()`     | Stop the SparkSession and release resources                     |

---

### 📎 Notes

* Only **one active SparkSession** should exist per application.
* Calling `getOrCreate()` ensures you **don't create duplicate sessions**.
* SparkSession automatically creates a `SparkContext` accessible via `spark.sparkContext`.

---

### 📌 SparkSession vs SparkContext

| SparkContext                | SparkSession                       |
| --------------------------- | ---------------------------------- |
| Entry point for RDD API     | Entry point for DataFrame API      |
| Used before Spark 2.0       | Introduced in Spark 2.0+           |
| Needs SQLContext separately | Unifies SQLContext and HiveContext |

---
## ⚙️ How to Pass Configurations in PySpark

In PySpark, configurations can be passed using the `SparkSession.builder.config()` method or via `SparkConf` (used with `SparkContext`).  
These configurations allow you to customize memory, shuffle behavior, parallelism, etc.

### ✅ Method 1: Using `SparkSession.builder.config()`

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ConfigExample") \
    .config("spark.executor.memory", "2g") \
    .config("spark.executor.cores", "2") \
    .config("spark.sql.shuffle.partitions", "50") \
    .getOrCreate()
````

| Config Key                     | Description                                 |
| ------------------------------ | ------------------------------------------- |
| `spark.executor.memory`        | Amount of memory per executor (e.g., 2g)    |
| `spark.executor.cores`         | Number of cores per executor                |
| `spark.sql.shuffle.partitions` | Number of partitions for shuffle operations |

### ✅ Method 2: Using `SparkConf` with `SparkContext`

```python
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

conf = SparkConf() \
    .setAppName("ConfigWithSparkConf") \
    .set("spark.executor.memory", "3g") \
    .set("spark.executor.instances", "4")

sc = SparkContext(conf=conf)

# Create SparkSession from existing SparkContext
spark = SparkSession(sc)
```

### 📌 Example: Read CSV with Configs

```python
spark = SparkSession.builder \
    .appName("ReadCSVWithConfig") \
    .config("spark.sql.shuffle.partitions", "10") \
    .getOrCreate()

df = spark.read.option("header", True).csv("data.csv")
df.show()
```
### ⚙️ General Application Configs

| Config Key               | Description                            | Example Value     | Code Example                                                                 |
|--------------------------|----------------------------------------|-------------------|------------------------------------------------------------------------------|
| `spark.app.name`         | Name of your Spark app                 | `MyApp`           | `SparkSession.builder.appName("MyApp")`                                     |
| `spark.master`           | Cluster manager                        | `local[*]`        | `SparkSession.builder.master("local[*]")`                                   |
| `spark.driver.memory`    | Memory for driver                      | `1g`              | `.config("spark.driver.memory", "1g")`                                      |
| `spark.driver.cores`     | Cores for driver (K8s)                 | `1`               | `.config("spark.driver.cores", "1")`                                        |
| `spark.driver.maxResultSize` | Max size of result from driver     | `1g`              | `.config("spark.driver.maxResultSize", "1g")`                               |

### 🧵 Executor Configs

| Config Key                 | Description                          | Example Value | Code Example                                        |
|----------------------------|--------------------------------------|---------------|-----------------------------------------------------|
| `spark.executor.memory`    | Memory per executor                  | `2g`          | `.config("spark.executor.memory", "2g")`            |
| `spark.executor.cores`     | Cores per executor                   | `2`           | `.config("spark.executor.cores", "2")`              |
| `spark.executor.instances` | Number of executors                  | `4`           | `.config("spark.executor.instances", "4")`          |
| `spark.executor.extraJavaOptions` | Extra JVM opts              | `-XX:+PrintGCDetails` | `.config("spark.executor.extraJavaOptions", "-XX:+PrintGCDetails")` |

### 🔄 Shuffle & Parallelism

| Config Key                     | Description                              | Example Value | Code Example                                           |
|--------------------------------|------------------------------------------|---------------|--------------------------------------------------------|
| `spark.default.parallelism`    | Default RDD partition count              | `8`           | `.config("spark.default.parallelism", "8")`            |
| `spark.sql.shuffle.partitions` | Partitions for SQL shuffles              | `200`         | `.config("spark.sql.shuffle.partitions", "200")`       |
| `spark.shuffle.compress`       | Enable shuffle compression               | `true`        | `.config("spark.shuffle.compress", "true")`            |
| `spark.shuffle.spill.compress` | Compress spilled shuffle data            | `true`        | `.config("spark.shuffle.spill.compress", "true")`      |

### 🧠 Memory Management

| Config Key                     | Description                              | Example Value | Code Example                                           |
|--------------------------------|------------------------------------------|---------------|--------------------------------------------------------|
| `spark.memory.fraction`        | JVM heap for execution + storage         | `0.6`         | `.config("spark.memory.fraction", "0.6")`              |
| `spark.memory.storageFraction` | JVM heap for cached data                 | `0.5`         | `.config("spark.memory.storageFraction", "0.5")`       |
| `spark.memory.offHeap.enabled` | Enable off-heap memory                   | `true`        | `.config("spark.memory.offHeap.enabled", "true")`      |
| `spark.memory.offHeap.size`    | Size of off-heap memory                  | `512m`        | `.config("spark.memory.offHeap.size", "512m")`         |

### 🗂️ Data Sources

| Config Key                              | Description                                | Example Value | Code Example                                           |
|-----------------------------------------|--------------------------------------------|---------------|--------------------------------------------------------|
| `spark.sql.sources.partitionOverwriteMode` | Overwrite mode                           | `dynamic`     | `.config("spark.sql.sources.partitionOverwriteMode", "dynamic")` |
| `spark.sql.files.maxPartitionBytes`    | Max size per file partition                | `134217728`   | `.config("spark.sql.files.maxPartitionBytes", "134217728")`       |
| `spark.sql.files.openCostInBytes`      | File open cost in bytes                    | `4194304`     | `.config("spark.sql.files.openCostInBytes", "4194304")`           |

### 🔐 Security

| Config Key                 | Description                              | Example Value | Code Example                                     |
|----------------------------|------------------------------------------|---------------|--------------------------------------------------|
| `spark.authenticate`       | Enable Spark authentication              | `true`        | `.config("spark.authenticate", "true")`          |
| `spark.authenticate.secret`| Shared secret for auth                   | `your_secret` | `.config("spark.authenticate.secret", "your_secret")` |
| `spark.ssl.enabled`        | Enable SSL                               | `true`        | `.config("spark.ssl.enabled", "true")`           |


### 🌐 External Systems (S3, Hive, etc.)

| Config Key                        | Description                              | Example Value       | Code Example                                                       |
|-----------------------------------|------------------------------------------|---------------------|--------------------------------------------------------------------|
| `spark.hadoop.fs.s3a.access.key`  | AWS access key                           | `AKIA...`           | `.config("spark.hadoop.fs.s3a.access.key", "AKIA...")`             |
| `spark.hadoop.fs.s3a.secret.key`  | AWS secret key                           | `xyz123...`         | `.config("spark.hadoop.fs.s3a.secret.key", "xyz123...")`           |
| `spark.sql.catalogImplementation`| Catalog impl: in-memory or hive          | `hive`              | `.config("spark.sql.catalogImplementation", "hive")`               |
| `spark.sql.warehouse.dir`        | Hive warehouse directory                 | `/user/hive/warehouse` | `.config("spark.sql.warehouse.dir", "/user/hive/warehouse")`     |



### 🧪 Debugging and Logging

| Config Key                | Description                           | Example Value       | Code Example                                      |
|---------------------------|---------------------------------------|---------------------|---------------------------------------------------|
| `spark.eventLog.enabled` | Enable Spark event logging            | `true`              | `.config("spark.eventLog.enabled", "true")`       |
| `spark.eventLog.dir`     | Location to store Spark event logs    | `hdfs:///spark/logs`| `.config("spark.eventLog.dir", "hdfs:///spark/logs")` |
| `spark.ui.enabled`       | Enable Spark Web UI                   | `true`              | `.config("spark.ui.enabled", "true")`             |
| `spark.ui.port`          | Port for Web UI                       | `4040`              | `.config("spark.ui.port", "4040")`                |


### 🛠️ Example: Full Config with SparkSession

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("FullConfigExample") \
    .master("local[*]") \
    .config("spark.executor.memory", "4g") \
    .config("spark.executor.cores", "2") \
    .config("spark.sql.shuffle.partitions", "50") \
    .config("spark.eventLog.enabled", "true") \
    .getOrCreate()




