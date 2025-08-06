
# 🏷️ PySpark Classes

---
PySpark is built using a set of core classes and APIs that enable distributed data processing. These classes represent entry points, data abstractions, configurations, and utilities that interact with the Spark engine.

---

## 🔰 Core PySpark Classes

| Class Name             | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `SparkSession`         | Entry point to DataFrame and SQL functionality                             |
| `SparkContext`         | Entry point to low-level Spark RDD API                                     |
| `RDD`                  | Immutable, distributed collection of objects                               |
| `DataFrame`            | Distributed data with schema; table-like                                   |
| `Row`                  | Represents a single row of a DataFrame                                     |
| `Column`               | Represents a column in a DataFrame, used in expressions                    |
| `StructType`           | Defines the schema of a DataFrame                                           |
| `StructField`          | Describes a field in the schema (name, type, nullable)                     |
| `SQLContext`           | Legacy class to work with structured data; replaced by `SparkSession`      |
| `DataFrameReader`      | Helps read data into a DataFrame                                            |
| `DataFrameWriter`      | Helps write DataFrame to external sources                                   |
| `Broadcast`            | Used to broadcast variables to all nodes                                   |
| `Accumulator`          | Used to accumulate values across workers (now deprecated in favor of AccumulatorV2) |
| `Window`               | Defines window specifications for window functions                         |
| `GroupData`            | Intermediate result after `groupBy`, supports aggregation functions         |

---

## 🔍 Example Usage of Common Classes

### ✅ SparkSession

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Example").getOrCreate()
````

### ✅ RDD

```python
rdd = spark.sparkContext.parallelize([1, 2, 3])
```

### ✅ DataFrame and Row

```python
from pyspark.sql import Row

data = [Row(name="Alice", age=30), Row(name="Bob", age=25)]
df = spark.createDataFrame(data)
df.show()
```

### ✅ StructType and StructField

```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

data = [("Alice", 30), ("Bob", 25)]
df = spark.createDataFrame(data, schema)
df.printSchema()
```

### ✅ Column Operations

```python
from pyspark.sql.functions import col

df.select(col("name"), col("age") + 1).show()
```

### ✅ Window Functions

```python
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

window_spec = Window.partitionBy("department").orderBy("salary")
df.withColumn("rank", row_number().over(window_spec)).show()
```

---

## 🧠 Summary

| Category          | Class Examples                       |
| ----------------- | ------------------------------------ |
| Entry Point       | `SparkSession`, `SparkContext`       |
| Data Abstraction  | `RDD`, `DataFrame`, `Row`, `Column`  |
| Schema Definition | `StructType`, `StructField`          |
| IO Helpers        | `DataFrameReader`, `DataFrameWriter` |
| Distributed Utils | `Broadcast`, `Accumulator`           |
| SQL & Windowing   | `SQLContext`, `Window`, `GroupData`  |
