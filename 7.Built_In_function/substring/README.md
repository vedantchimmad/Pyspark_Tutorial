# ✂️ `substring` in PySpark

---

## 📝 Overview
The `substring` function in PySpark extracts a **substring** from a string column starting from a given position for a given length.

**Import Path**
```python
from pyspark.sql.functions import substring
````

---

## 🛠 Syntax

```python
substring(str, pos, len)
```

| Parameter | Description                                                |
| --------- | ---------------------------------------------------------- |
| `str`     | **Required**. Column or string expression to extract from. |
| `pos`     | **Required**. Starting position (1-based index).           |
| `len`     | **Required**. Number of characters to extract.             |

**Return Type:**
`StringType`

---

## ⚠ Important Notes

* The starting position `pos` is **1-based**, not 0-based.
* If `pos` is negative, it counts from the **end** of the string.
* If `len` exceeds available characters, it returns up to the end of the string.

---

## 🎯 Example 1: Basic Substring

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import substring

spark = SparkSession.builder.appName("SubstringExample").getOrCreate()

data = [("Apache Spark",), ("PySpark SQL",)]
df = spark.createDataFrame(data, ["text"])

df = df.withColumn(
    "sub_text",
    substring("text", 1, 6)  # First 6 characters
)

df.show(truncate=False)
```

**Output:**

```
+-------------+-------+
|text         |sub_text|
+-------------+-------+
|Apache Spark |Apache |
|PySpark SQL  |PySpar |
+-------------+-------+
```

---

## 🎯 Example 2: Starting from Middle

```python
df = df.withColumn(
    "middle_part",
    substring("text", 8, 5)  # Start from 8th char, take 5 chars
)

df.show(truncate=False)
```

**Output:**

```
+-------------+-------+-----------+
|text         |sub_text|middle_part|
+-------------+-------+-----------+
|Apache Spark |Apache |Spark      |
|PySpark SQL  |PySpar | SQL       |
+-------------+-------+-----------+
```

---

## 🎯 Example 3: Negative Position

```python
data = [("DataProcessing",)]
df = spark.createDataFrame(data, ["word"])

df = df.withColumn(
    "last_4",
    substring("word", -4, 4)  # Last 4 characters
)

df.show()
```

**Output:**

```
+--------------+------+
|word          |last_4|
+--------------+------+
|DataProcessing|sing  |
+--------------+------+
```

---

## 🎯 Example 4: With Literal Strings

```python
from pyspark.sql.functions import lit

df = spark.range(1).withColumn(
    "example",
    substring(lit("HelloWorld"), 1, 5)
)

df.show()
```

**Output:**

```
+---+-------+
| id|example|
+---+-------+
|  0|Hello  |
+---+-------+
```

---

## 🔍 Key Points

* `substring` is **position-based**, not pattern-based (use `regexp_extract` for regex).
* Works with **negative indexing** from the end.
* Ideal for:

    * Extracting parts of fixed-format strings.
    * Cutting IDs, codes, or names to a specific length.
    * Preprocessing for data cleansing.

---

