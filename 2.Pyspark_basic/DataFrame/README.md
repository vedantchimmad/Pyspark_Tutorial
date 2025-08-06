# 🧾 DataFrame in PySpark

---
### 📘 What is a DataFrame?

A **DataFrame** in PySpark is a distributed collection of **data organized into named columns**, similar to a table in a relational database or a DataFrame in pandas.

It is built on top of **RDDs** and supports:
- Optimized execution via **Catalyst Optimizer**
- SQL queries
- Interoperability with Hive, Avro, Parquet, ORC, etc.

---

### 🧩 Core Features

| Feature                    | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| 📐 **Schema Support**       | DataFrames have named columns with defined data types                       |
| ⚙️ **Optimized Execution**   | Uses Catalyst Optimizer and Tungsten engine for performance improvement     |
| 🧠 **Lazy Evaluation**       | Operations are not executed until an action is called                        |
| ⛓️ **Transformations & Actions** | Supports chaining of high-level transformations and actions          |
| 🗃️ **Data Source Integration**| Read/write from multiple sources (CSV, Parquet, JSON, Hive, etc.)         |
| 🧾 **SQL Query Support**     | You can register DataFrames as temporary views and run SQL queries          |
| 🌐 **Cross-Language Support**| APIs available in Python, Scala, Java, R                                    |
| 🧪 **Strong Integration with Spark SQL** | Enables analytical queries, aggregations, and joins                |
| ⚡ **In-Memory Computation** | Stores intermediate data in memory for fast processing                      |
| 🔁 **Interoperability with RDDs**| Easily convert between DataFrames and RDDs                             |
| 📊 **Built-in Aggregations** | Provides functions like `groupBy`, `agg`, `count`, `avg`, `sum`, etc.       |
| 🧼 **Schema Inference**      | Can automatically infer schema from data (e.g., `inferSchema=True`)         |
| 📦 **Serialization Support** | Efficient serialization using Encoders (especially in Scala/Java)          |
| 📄 **Supports UDFs**         | Use User Defined Functions for custom transformations                      |
| 🔄 **Supports Streaming**    | DataFrames support structured streaming for real-time data processing       |

---

### 🧱 Creating DataFrames

### ✅1. From List of Tuples

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DFExample").getOrCreate()

data = [(1, "Alice"), (2, "Bob")]
df = spark.createDataFrame(data, ["id", "name"])
df.show()
````

### ✅2. From RDD

```python
rdd = spark.sparkContext.parallelize([(3, "Charlie"), (4, "David")])
df_from_rdd = rdd.toDF(["id", "name"])
```

### ✅3. From CSV File

```python
df = spark.read.csv("data.csv", header=True, inferSchema=True)
```

---

### 🔄 Common DataFrame Operations

| Operation           | Example                                           |
| ------------------- | ------------------------------------------------- |
| Show data           | `df.show()`                                       |
| Print schema        | `df.printSchema()`                                |
| Select columns      | `df.select("name")`                               |
| Filter rows         | `df.filter(df["age"] > 25)`                       |
| Add new column      | `df.withColumn("new", df["age"] + 1)`             |
| Rename column       | `df.withColumnRenamed("old", "new")`              |
| Drop column         | `df.drop("column_name")`                          |
| Sort data           | `df.sort(df["age"].desc())`                       |
| Group and aggregate | `df.groupBy("department").agg({"salary": "avg"})` |
| Join                | `df1.join(df2, df1.id == df2.id, "inner")`        |

---

### 🧪 SQL with DataFrames

```python
df.createOrReplaceTempView("people")
result = spark.sql("SELECT name FROM people WHERE age > 25")
result.show()
```

---

### 🔄 DataFrame to RDD and Pandas

```python
# To RDD
rdd = df.rdd

# To Pandas
pandas_df = df.toPandas()
```

---

### 🧠 When to Use DataFrame?

| Use Case                            | Why DataFrame?                  |
| ----------------------------------- | ------------------------------- |
| Structured data                     | Automatically infers schema     |
| Performance-critical tasks          | Catalyst optimizer boosts speed |
| SQL or declarative queries          | Easy with SQL integration       |
| Working with different file formats | Parquet, ORC, Avro, etc.        |

---

### ❗ Limitations

* Cannot handle unstructured data easily (use RDDs instead)
* Transformations are abstract; need attention to schema
* Python UDFs can reduce performance (use built-in functions where possible)

---

### 🛠️ Example: DataFrame End-to-End

```python
df = spark.read.csv("employees.csv", header=True, inferSchema=True)

# Schema support
df.printSchema()

# Optimized transformation
df_filtered = df.filter(df["age"] > 30).select("name", "age")

# SQL Integration
df.createOrReplaceTempView("emp")
spark.sql("SELECT name FROM emp WHERE age > 30").show()
```


