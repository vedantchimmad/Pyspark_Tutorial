# 🔍 `regexp_replace` in PySpark

---

## 📝 Overview
The `regexp_replace` function in PySpark replaces **all substrings** in a string that match a given **regular expression pattern** with a replacement string.  
Think of it as a **find-and-replace** operation powered by regex.

**Import Path**
```python
from pyspark.sql.functions import regexp_replace
````

---

## 🛠 Syntax

```python
regexp_replace(str, pattern, replacement)
```

| Parameter     | Description                                   |
| ------------- | --------------------------------------------- |
| `str`         | **Required**. Column containing the string.   |
| `pattern`     | **Required**. Regex pattern to search for.    |
| `replacement` | **Required**. String to replace matches with. |

**Return Type:**
`StringType`

---

## 🎯 Example 1: Replace a Specific Word

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace

spark = SparkSession.builder.appName("RegexReplaceExample").getOrCreate()

data = [("Apache Spark",), ("Spark SQL",)]
df = spark.createDataFrame(data, ["text"])

df = df.withColumn(
    "updated_text",
    regexp_replace("text", "Spark", "PySpark")
)

df.show()
```

**Output:**

```
+-------------+-------------+
|text         |updated_text |
+-------------+-------------+
|Apache Spark |Apache PySpark|
|Spark SQL    |PySpark SQL  |
+-------------+-------------+
```

---

## 🎯 Example 2: Remove Special Characters

```python
data = [("Hello@World!",), ("Py$Spark#",)]
df = spark.createDataFrame(data, ["text"])

df = df.withColumn(
    "clean_text",
    regexp_replace("text", "[^a-zA-Z0-9 ]", "")  # Keep only letters/numbers/spaces
)

df.show()
```

**Output:**

```
+------------+-----------+
|text        |clean_text |
+------------+-----------+
|Hello@World!|HelloWorld |
|Py$Spark#   |PySpark    |
+------------+-----------+
```

---

## 🎯 Example 3: Mask Phone Numbers

```python
data = [("Call me at 9876543210",)]
df = spark.createDataFrame(data, ["message"])

df = df.withColumn(
    "masked",
    regexp_replace("message", "\\d{10}", "**********")
)

df.show()
```

**Output:**

```
+-----------------------+------------------+
|message                |masked            |
+-----------------------+------------------+
|Call me at 9876543210  |Call me at **********|
+-----------------------+------------------+
```

---

## 🔍 Key Points

* **Regex-powered:** Supports full regular expressions for flexible matching.
* **Global replacement:** Replaces **all occurrences**, not just the first.
* **Escaping:** Remember to double escape (`\\`) special regex characters in Python strings.
* Useful for:

    * Data cleaning (removing unwanted characters)
    * Masking sensitive data
    * Text normalization

---

