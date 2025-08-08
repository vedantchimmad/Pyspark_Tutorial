# 🗂️ PySpark `partitionBy()`

---
The **`partitionBy()`** function in PySpark is used to **partition** data when writing it out to storage.  
It organizes the output files into separate folders based on **column values**, which helps in **query performance** and **data management**.

---

## 🛠 Syntax

```python
DataFrameWriter.partitionBy(*cols)
````

| Parameter | Description                                                      |
| --------- | ---------------------------------------------------------------- |
| `*cols`   | One or more column names by which to partition the output files. |

---

## 🔍 Key Points

* **Used only with `write` operations** (`.write.partitionBy(...)`).
* Creates **sub-directories** for each unique value in the partition column(s).
* Helps in **data skipping** during queries (e.g., in Hive, Spark SQL, Presto).
* Can partition by multiple columns.
* Works with file formats like **Parquet**, **ORC**, **Avro**, **CSV** (best with columnar formats like Parquet/ORC).

---

## 📌 Example 1: Partition by Single Column

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PartitionByExample").getOrCreate()

data = [
    ("John", "USA", 25),
    ("Mike", "USA", 30),
    ("Sara", "UK", 22),
    ("Anna", "UK", 28)
]
df = spark.createDataFrame(data, ["name", "country", "age"])

# Write partitioned by country
df.write.mode("overwrite").partitionBy("country").parquet("/tmp/output_partitioned")
```

**Output directory structure:**

```
/tmp/output_partitioned/
    country=UK/
        part-0000.parquet
    country=USA/
        part-0000.parquet
```

---

## 📌 Example 2: Partition by Multiple Columns

```python
df.write.mode("overwrite").partitionBy("country", "age").parquet("/tmp/output_multi_partition")
```

**Output directory structure:**

```
/tmp/output_multi_partition/
    country=UK/age=22/
    country=UK/age=28/
    country=USA/age=25/
    country=USA/age=30/
```

---

## 📌 Example 3: Reading Partitioned Data

```python
df_read = spark.read.parquet("/tmp/output_partitioned")
df_read.show()
```

Spark will **automatically detect** and **read partition columns**.

---

## ⚡ Performance Tips

* Choose partition columns with **low to medium cardinality** (e.g., country, year)
  → Avoid very high cardinality like `user_id` because it can create **too many small files**.
* Combine with **bucketBy** when needed for better join performance.
* For querying, partition pruning will **skip irrelevant partitions** and improve speed.

---

## 📌 Summary Table

| Feature             | Description                                         |
| ------------------- | --------------------------------------------------- |
| Purpose             | Organize output files into folders by column values |
| Works With          | `.write` in Spark DataFrameWriter                   |
| Best Formats        | Parquet, ORC                                        |
| Multiple Columns    | Supported                                           |
| Performance Benefit | Partition pruning, faster queries                   |
| Caution             | Avoid high-cardinality partition columns            |

---
