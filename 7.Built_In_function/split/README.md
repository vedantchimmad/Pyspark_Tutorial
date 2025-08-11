# ✂️ `split` in PySpark

---

## 📝 Overview
The `split` function in PySpark splits a string **column** into an **array** of substrings based on a **delimiter** or **regular expression pattern**.

**Import Path**
```python
from pyspark.sql.functions import split
````

---

## 🛠 Syntax

```python
split(str, pattern, limit=-1)
```

| Parameter | Description                                                   |
| --------- | ------------------------------------------------------------- |
| `str`     | **Required**. Column containing the string to split.          |
| `pattern` | **Required**. Delimiter or regex pattern for splitting.       |
| `limit`   | Optional. Maximum number of splits. Default: `-1` (no limit). |

**Return Type:**
`ArrayType(StringType)`

---

## 🎯 Example 1: Split by Space

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import split

spark = SparkSession.builder.appName("SplitExample").getOrCreate()

data = [("Apache Spark Framework",), ("PySpark SQL Functions",)]
df = spark.createDataFrame(data, ["text"])

df = df.withColumn(
    "words",
    split("text", " ")
)

df.show(truncate=False)
```

**Output:**

```
+-----------------------+----------------------------+
|text                   |words                       |
+-----------------------+----------------------------+
|Apache Spark Framework |[Apache, Spark, Framework]  |
|PySpark SQL Functions  |[PySpark, SQL, Functions]   |
+-----------------------+----------------------------+
```

---

## 🎯 Example 2: Split by Comma

```python
data = [("apple,banana,orange",)]
df = spark.createDataFrame(data, ["fruits"])

df = df.withColumn(
    "fruit_list",
    split("fruits", ",")
)

df.show(truncate=False)
```

**Output:**

```
+-------------------+----------------------+
|fruits             |fruit_list            |
+-------------------+----------------------+
|apple,banana,orange|[apple, banana, orange]|
+-------------------+----------------------+
```

---

## 🎯 Example 3: Split with Limit

```python
data = [("one,two,three,four",)]
df = spark.createDataFrame(data, ["numbers"])

df = df.withColumn(
    "limited_split",
    split("numbers", ",", 2)  # Split into only 2 parts
)

df.show(truncate=False)
```

**Output:**

```
+-------------------+----------------+
|numbers            |limited_split   |
+-------------------+----------------+
|one,two,three,four |[one, two,three,four]|
+-------------------+----------------+
```

---

## 🎯 Example 4: Regex Split

```python
data = [("word1;word2|word3,word4",)]
df = spark.createDataFrame(data, ["text"])

df = df.withColumn(
    "words",
    split("text", "[;|,]")  # Split by ; or | or ,
)

df.show(truncate=False)
```

**Output:**

```
+---------------------+---------------------+
|text                 |words                |
+---------------------+---------------------+
|word1;word2|word3,word4|[word1, word2, word3, word4]|
+---------------------+---------------------+
```

---

## 🔍 Key Points

* Returns an **array column**, which can be processed further using `explode`, `size`, or indexing (`col("array")[n]`).
* Supports **regex patterns** for flexible splitting.
* The `limit` parameter helps control how many splits occur.
* Useful for:

    * Breaking down CSV-style fields
    * Tokenizing text
    * Parsing structured strings

---


