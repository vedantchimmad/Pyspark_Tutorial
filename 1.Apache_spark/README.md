# ⚡ Apache Spark

---

Apache **Spark** is an open-source distributed computing system used for big data processing and analytics. It provides an interface for programming entire clusters with implicit data parallelism and fault tolerance.

## 🔹 Key Features of Apache Spark

| Feature                 | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| **In-Memory Computing** | Processes data in memory, reducing disk I/O for faster performance          |
| **Speed**               | 100x faster than Hadoop MapReduce for in-memory, 10x on disk                |
| **Ease of Use**         | High-level APIs in Python, Scala, Java, and R                               |
| **Unified Engine**      | Single platform for batch, streaming, ML, and graph processing              |
| **Distributed Processing** | Runs on clusters, scales horizontally for large datasets                  |
| **Fault Tolerance**     | Uses RDD lineage to recover from node failures                              |
| **Lazy Evaluation**     | Optimizes computation by delaying execution until an action is called       |
| **Built-in Libraries**  | Includes SQL, MLlib (Machine Learning), GraphX, and Spark Streaming         |
| **Compatible with Hadoop** | Can run on Hadoop YARN, read HDFS, and access data from Hive              |
| **Streaming Capability**| Handles real-time data using Spark Streaming or Structured Streaming        |

---

## ✅ Advantages of Using Apache Spark

1. **High Performance**
    - In-memory computation boosts processing speed significantly.
    - Better optimized execution using DAG scheduler and Catalyst optimizer.

2. **Ease of Development**
    - Simple APIs for complex data workflows using Python (`PySpark`), Scala, etc.
    - Rich set of built-in transformations and actions.

3. **Scalability**
    - Easily scales from a single machine to thousands of nodes.

4. **Advanced Analytics**
    - Supports machine learning, graph analytics, real-time stream processing—all in one engine.

5. **Unified Framework**
    - Single engine for handling batch jobs, interactive queries, real-time analytics, and machine learning.

6. **Fault Tolerance**
    - Automatically recovers lost data using lineage of operations.

7. **Community Support**
    - Strong open-source community and industry adoption.

8. **Integration**
    - Compatible with Hadoop, Hive, HBase, Cassandra, S3, and many other data sources.

---
## ⚙️ Apache Spark Architecture

Apache Spark follows a **master-slave architecture** consisting of a central coordinator called the **Driver** and many distributed workers called **Executors**.

### 🧱 Core Components

#### 1. **Driver Program**
- The entry point of a Spark application.
- Responsible for:
   - Converting user code into a Directed Acyclic Graph (DAG)
   - Scheduling tasks to be run on the cluster
   - Coordinating execution and collecting results

#### 2. **Cluster Manager**
- Allocates resources across applications.
- Types of cluster managers supported:
   - Spark Standalone
   - Apache Mesos
   - Hadoop YARN
   - Kubernetes

#### 3. **Executors**
- Distributed agents that run the tasks.
- Each executor is responsible for:
   - Running tasks assigned by the driver
   - Storing data in memory or disk storage
   - Reporting status back to the driver

#### 4. **Tasks**
- Units of work sent by the driver to executors.
- Each task is part of a stage derived from the DAG.


### 🖼 Spark Architecture Diagram

![Spark Architecture Diagram](../resource/image/spark_architecture.png)



### 🔁 Flow of Execution

1. **SparkContext** is created in the driver program.
2. The driver contacts the **cluster manager** to request resources.
3. **Executors** are launched on worker nodes.
4. The driver splits the job into **tasks** based on transformations and actions.
5. **Tasks are scheduled** and sent to the executors.
6. Executors run the tasks and send results back to the driver.

---

### 📌 Summary

| Component       | Role                                                  |
|----------------|-------------------------------------------------------|
| **Driver**      | Converts job into tasks, manages execution           |
| **Cluster Manager** | Allocates resources                              |
| **Executors**   | Perform computation and data storage                 |
| **Tasks**       | Smallest units of work executed on executors         |

---
## 🚀 Apache Spark Terminologies

---
Apache Spark is a powerful open-source engine used for big data processing. Below are key terminologies frequently used when working with Spark.


### 1. 🔹 RDD (Resilient Distributed Dataset)

* Fundamental data structure in Spark.
* Immutable distributed collection of objects that can be processed in parallel.
* Supports fault tolerance and in-memory computations.


### 2. 🔹 DataFrame

* Distributed collection of data organized into named columns (like a table in a relational database).
* Built on top of RDDs with optimizations via Catalyst engine.
* Can be created from various sources like JSON, Hive, Parquet, etc.

### 3. 🔹 Dataset

* Type-safe version of DataFrame (available in Scala and Java).
* Combines benefits of RDDs (type-safety) and DataFrames (optimizations).


### 4. 🔹 Transformation

* Operations that create a new RDD/DataFrame from an existing one.
* They are **lazy** (executed only when an action is triggered).
* Examples: `map()`, `filter()`, `flatMap()`, `groupByKey()`

### 5. 🔹 Action

* Operations that trigger execution of transformations and return values.
* Examples: `collect()`, `count()`, `reduce()`, `first()`, `saveAsTextFile()`

### 6. 🔹 Lazy Evaluation

* Spark does not execute transformations immediately.
* Execution starts only when an action is invoked.


### 7. 🔹 SparkSession

* Entry point to use Spark functionality (introduced in Spark 2.0).
* Replaces older `SparkContext`, `SQLContext`, and `HiveContext`.

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Example").getOrCreate()
```


### 8. 🔹 DAG (Directed Acyclic Graph)

* Execution plan for a sequence of computations.
* Spark builds a DAG of stages for all jobs to be executed.

### 9. 🔹 Executor

* A worker node process responsible for running individual tasks in a job.
* Each application has its own executors.

### 10. 🔹 Driver

* The master process that coordinates workers, schedules tasks, and tracks their progress.


### 11. 🔹 Task

* A single unit of work sent to executors.
* Each stage is divided into tasks.

### 12. 🔹 Partition

* Logical division of data in RDD/DataFrame.
* Spark automatically divides data across partitions for parallel processing.


### 13. 🔹 Shuffle

* Re-distribution of data across partitions (usually for aggregations or joins).
* Costly operation, should be minimized when possible.


### 14. 🔹 Broadcast Variable

* Read-only variable cached on each machine rather than shipping a copy with tasks.


### 15. 🔹 Accumulator

* Write-only shared variable used to aggregate information across executors.

### 16. 🔹 Cluster Manager

* External service responsible for acquiring resources on the cluster.
* Types: **Standalone**, **YARN**, **Mesos**, **Kubernetes**

### 17. 🔹 Job

* A high-level action submitted by the user.

### 18. 🔹 Stage

* Each job is divided into multiple stages based on shuffle boundaries.

---

## ⚙️ Cluster Manager Types in Apache Spark

---

Apache Spark supports multiple **cluster managers** that handle resource allocation across the cluster. A **cluster manager** is responsible for acquiring resources on the cluster and launching executors.

---

### 🔹 1. **Standalone Cluster Manager**

- Spark’s **built-in** cluster manager.
- Easy to set up and manage.
- Suitable for small or medium deployments.

> ✅ Good for development/testing or small-scale production workloads.

---

### 🔹 2. **Apache Hadoop YARN (Yet Another Resource Negotiator)**

- Integrates Spark with **Hadoop ecosystem**.
- Spark can run as an application on YARN.
- Allows Spark to share resources with other applications.

> 🔗 Used in many enterprises with Hadoop clusters.

---

### 🔹 3. **Apache Mesos**

- General-purpose cluster manager.
- Can run multiple types of workloads like Spark, Hadoop, Kafka, etc.
- Offers **fine-grained sharing** of resources.

> 🧠 Complex setup, good for large and diverse workloads.

---

### 🔹 4. **Kubernetes**

- Container-based cluster manager.
- Spark runs inside containers (Pods).
- Leverages container orchestration, scaling, and isolation.

> 🚀 Growing in popularity for **cloud-native** and **containerized** workloads.

### 5. 🖥️ **Local Mode**

### ✅ What is it?
Runs Spark on a **single machine** without any external cluster manager.

#### 🔧 Configuration
```python
.master("local[*]")  # Use all cores
.master("local[2]")  # Use 2 threads
```
---

### 🔸 Summary Comparison

| Cluster Manager | Built-in | Supports Multi-Tenant | Container Support | Cloud Native |
|-----------------|----------|------------------------|-------------------|--------------|
| Standalone      | ✅       | ❌                     | ⚠️ Partial         | ❌           |
| YARN            | ❌       | ✅                     | ❌                | ❌           |
| Mesos           | ❌       | ✅                     | ⚠️ Limited         | ❌           |
| Kubernetes      | ❌       | ✅                     | ✅                | ✅           |

---

> 📝 **Note**: Choosing the right cluster manager depends on your existing infrastructure, team expertise, and workload requirements.
---

## 🔄 Apache Spark Ecosystem

---

The **Apache Spark Ecosystem** is a powerful suite of tools and libraries designed to handle large-scale data processing across various domains such as batch processing, streaming, machine learning, and graph analytics.


### 🧩 Core Components of Spark Ecosystem


#### ⚙️ 1. **Spark Core**

* The base engine for Spark applications.
* Provides:

    * Memory management
    * Fault recovery
    * Task scheduling
    * Interaction with storage systems (HDFS, S3, etc.)

```python
from pyspark import SparkContext
sc = SparkContext("local", "App")
```

---

#### 📊 2. **Spark SQL**

* Enables querying structured/semi-structured data using SQL.
* Supports integration with Hive, Avro, Parquet, ORC, JSON.

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("SQLApp").getOrCreate()
df = spark.read.json("data.json")
df.createOrReplaceTempView("data")
spark.sql("SELECT * FROM data").show()
```

---

#### 💧 3. **Spark Streaming**

* Processes real-time data streams (e.g., from Kafka, Flume, sockets).
* Uses micro-batch processing.

```python
from pyspark.streaming import StreamingContext
ssc = StreamingContext(sc, 1)  # 1 second batch interval
lines = ssc.socketTextStream("localhost", 9999)
```

---

##### 🔁 4. **MLlib (Machine Learning Library)**

* Scalable ML algorithms including:

    * Classification
    * Regression
    * Clustering
    * Dimensionality Reduction

```python
from pyspark.ml.classification import LogisticRegression
lr = LogisticRegression()
model = lr.fit(training_data)
```

---

### 🔗 5. **GraphX**

* Distributed graph computation engine.
* Runs on top of Spark Core (only available in Scala).

> 🚫 Not available in PySpark directly

---

### 🔌 6. **SparkR**

* R API for Spark.
* Allows R users to run distributed computations using Spark.

```r
library(SparkR)
sparkR.session()
df <- read.df("data.csv", source = "csv", inferSchema = "true", header = "true")
```

---

#### 📦 7. **Delta Lake**

* Open-source storage layer that brings ACID transactions to Spark & big data lakes.

```python
from delta import configure_spark_with_delta_pip
spark = configure_spark_with_delta_pip(builder).getOrCreate()
```

---

### 🖼️ Ecosystem Diagram

```
+---------------------+
|     User APIs       |
|---------------------|
| SQL | DataFrames | RDDs |
+---------------------+
        ↓
+---------------------+
|   Spark Core Engine |
+---------------------+
 ↓      ↓       ↓     ↓
SQL   MLlib   GraphX  Streaming
```

> 💡 Add-ons like **Delta Lake**, **Hudi**, and **Iceberg** extend Spark’s capabilities for modern data lakes.

---

### ✅ Summary

| Component       | Purpose                                |
| --------------- | -------------------------------------- |
| Spark Core      | Core functionality (execution, memory) |
| Spark SQL       | SQL/structured data processing         |
| Spark Streaming | Real-time stream processing            |
| MLlib           | Machine learning library               |
| GraphX          | Graph computation                      |
| SparkR          | R interface                            |
| Delta Lake      | ACID on data lakes                     |

---

> 🧠 The ecosystem empowers Spark to be a **unified engine** for big data analytics across batch, streaming, SQL, and ML workloads.

## Spark Memory Management

---

Memory management is a crucial aspect of Apache Spark performance. Spark does **in-memory computation**, so how memory is allocated impacts the speed and efficiency of your applications.

---

### Types of Memory in Spark

Spark divides memory into two main regions:

#### 1. **Execution Memory**
- Used for computation like **shuffles**, **joins**, **sorts**, and **aggregations**.
- Temporarily stores data during tasks' execution.

#### 2. **Storage Memory**
- Used for **caching** and **persisting** RDDs/DataFrames.
- Holds the contents of broadcast variables.

---

## Unified Memory Management (From Spark 1.6+)

Spark uses a **unified memory model**, dividing the available memory into:

| Memory Region     | Description                                                  |
|-------------------|--------------------------------------------------------------|
| Reserved Memory   | Fixed size memory reserved for Spark internals (not tunable) |
| User Memory       | For internal metadata, UDFs, data structures (10% by default)|
| Spark Memory      | Main memory shared between storage and execution             |

**Spark Memory** is further split into:
- **Execution Memory**
- **Storage Memory**

Spark tries to **dynamically share** the memory between execution and storage based on demand.

---

### Memory Distribution (Default)

Example with 1 GB total executor memory:

| Memory Category   | Size         |
|-------------------|--------------|
| Reserved Memory   | ~300 MB      |
| Usable Memory     | ~700 MB      |
| User Memory (10%) | ~70 MB       |
| Spark Memory (90%)| ~630 MB      |
| ↳ Storage Memory  | dynamic      |
| ↳ Execution Memory| dynamic      |

---

### Tuning Memory in Spark

You can configure memory management using:

| Property                          | Description                                       |
|----------------------------------|---------------------------------------------------|
| `spark.executor.memory`          | Total memory per executor                         |
| `spark.memory.fraction`          | Fraction of executor memory used for Spark memory (default: 0.6) |
| `spark.memory.storageFraction`   | Fraction of Spark memory for storage (default: 0.5) |
| `spark.executor.pyspark.memory`  | Additional memory for Python worker processes     |

---

### Tips for Efficient Memory Usage

- Use `.persist()` or `.cache()` only when necessary.
- Unpersist unused RDDs/DataFrames.
- Avoid wide transformations that cause heavy shuffles.
- Tune memory settings based on workload patterns.
- Monitor with Spark UI (Storage tab, Executors tab).

---

### Visual Overview

```text
+-----------------------------------------------------+
|                    Executor Memory (1 GB)           |
+-------------------------+---------------------------+
| Reserved Memory (~300MB)| Usable Memory (~700MB)    |
|                         +---------------------------+
|                         |  User Memory (10%)        |
|                         +---------------------------+
|                         |  Spark Memory (90%)       |
|                         |  +---------------------+  |
|                         |  | Execution Memory     |  |
|                         |  | Storage Memory       |  |
|                         |  +---------------------+  |
+-------------------------+---------------------------+
```
```text
Total: 1GB
│
├── Reserved Memory (≈ 300MB)  ← Not configurable
│
└── Usable Memory (≈ 700MB)
    ├── User Memory (10%) ≈ 70MB  ← Custom variables, accumulators
    └── Spark Memory (90%) ≈ 630MB
        ├── Execution Memory   ← Joins, aggregations, shuffles
        └── Storage Memory     ← Caching, persist, broadcast

```
### 📐 Configuration Reference
| Config Name                    | Default | Description                                              |
| ------------------------------ | ------- | -------------------------------------------------------- |
| `spark.executor.memory`        | `1g`    | Total memory per executor                                |
| `spark.memory.fraction`        | `0.6`   | Fraction of usable memory used for execution + storage   |
| `spark.memory.storageFraction` | `0.5`   | Fraction of spark memory set aside for storage initially |

### 🧪 Example: Understanding Spark Memory via Code

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Step 1: Create Spark Session with limited memory to observe usage
spark = SparkSession.builder
    .appName("DataFrameMemoryExample")
    .config("spark.executor.memory", "1g")
    .config("spark.memory.fraction", "0.6")
    .config("spark.memory.storageFraction", "0.5")
    .getOrCreate()

# Step 2: Create DataFrame with sample data
data = [(i,) for i in range(1, 1000000)]
df = spark.createDataFrame(data, ["number"])

# 🔸 Execution Memory: Used during transformations
# e.g. filters, aggregations, joins
filtered_df = df.filter(col("number") % 2 == 0)

# 🔸 Storage Memory: Used when we cache/persist a DataFrame
filtered_df.cache()
filtered_df.count()  # Triggers actual caching

# 🔸 User Memory: Broadcast variable or accumulator
# Broadcast variables store user-defined objects across nodes
factors = {"multiplier": 3}
broadcast_var = spark.sparkContext.broadcast(factors)

# Apply broadcast in transformation (execution memory again)
final_df = filtered_df.withColumn("tripled", col("number") * broadcast_var.value["multiplier"])

# Perform action to trigger execution
final_df.show(5)

# Cleanup
spark.stop()
```