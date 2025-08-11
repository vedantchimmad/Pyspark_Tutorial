# 🪄 `overlay` in PySpark

---

## 📝 Overview
The `overlay` function in PySpark replaces a substring of a string with another string starting at a given position and for a given length.  
Think of it as a "string patch" operation.

**Import Path**
```python
from pyspark.sql.functions import overlay
````

---

## 🛠 Syntax

```python
overlay(src, replaceString, pos, len= -1)
```

| Parameter       | Description                                                                           |
| --------------- | ------------------------------------------------------------------------------------- |
| `src`           | **Required**. Column containing the original string.                                  |
| `replaceString` | **Required**. The string to overlay/replace with.                                     |
| `pos`           | **Required**. Position (1-based index) in the string where replacement starts.        |
| `len`           | **Optional**. Number of characters to replace. Default `-1` means till end of string. |

**Return Type:**
`StringType`

---

## 🎯 Example 1: Basic Replacement

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import overlay

spark = SparkSession.builder.appName("OverlayExample").getOrCreate()

data = [("SparkSQL",), ("PySpark",)]
df = spark.createDataFrame(data, ["original"])

df = df.withColumn(
    "overlayed",
    overlay("original", "Python", 3, 4)  # Replace from position 3, length 4
)

df.show()
```

**Output:**

```
+--------+--------+
|original|overlayed|
+--------+--------+
|SparkSQL|SpPythonL|
|PySpark |PyPython |
+--------+--------+
```

---

## 🎯 Example 2: Insert Without Removing (len=0)

```python
data = [("SparkSQL",)]
df = spark.createDataFrame(data, ["original"])

df = df.withColumn(
    "inserted",
    overlay("original", "_v3_", 6, 0)  # Insert at position 6 without replacing
)

df.show()
```

**Output:**

```
+--------+-----------+
|original|inserted   |
+--------+-----------+
|SparkSQL|Spark_v3_SQL|
+--------+-----------+
```

---

## 🎯 Example 3: Replace Till End

```python
data = [("PySparkData",)]
df = spark.createDataFrame(data, ["original"])

df = df.withColumn(
    "till_end",
    overlay("original", "X", 5)  # Default len = -1, replaces till end
)

df.show()
```

**Output:**

```
+-----------+-------+
|original   |till_end|
+-----------+-------+
|PySparkData|PySpX  |
+-----------+-------+
```

---

## 🔍 Key Points

* **Position is 1-based**, so `pos=1` means replacement starts from the first character.
* If `len` exceeds the remaining string length, it will replace till the end.
* Works only with **string columns**.
* Useful for **string patching**, **masking sensitive data**, and **formatting outputs**.

---
