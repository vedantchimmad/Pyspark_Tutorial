# 🧮 `expr` in PySpark

---

## 📝 Overview
The `expr` function allows you to **use SQL expressions directly inside PySpark code**.  
It is handy when you want to write transformations in **SQL syntax** while still working in the DataFrame API.

**Import Path**
```python
from pyspark.sql import functions as F
````

---

## 🛠 Syntax

```python
expr(sql_expression)
```

| Parameter        | Description                                               |
| ---------------- | --------------------------------------------------------- |
| `sql_expression` | **Required**. A string containing a valid SQL expression. |

**Return Type:**
Depends on the SQL expression output.

---

## 🎯 Example 1: Simple Column Arithmetic

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("ExprExample").getOrCreate()

data = [(1, 10), (2, 20), (3, 30)]
df = spark.createDataFrame(data, ["id", "value"])

# Using expr to calculate new column
result = df.withColumn("double_value", F.expr("value * 2"))

result.show()
```

**Output:**

```
+---+-----+------------+
|id |value|double_value|
+---+-----+------------+
|1  |10   |20          |
|2  |20   |40          |
|3  |30   |60          |
+---+-----+------------+
```

---

## 🎯 Example 2: Using SQL Functions

```python
data = [("2025-08-11",), ("2025-01-01",)]
df = spark.createDataFrame(data, ["date_str"])

result = df.withColumn("month_name", F.expr("date_format(date_str, 'MMMM')"))

result.show()
```

**Output:**

```
+----------+-----------+
|date_str  |month_name |
+----------+-----------+
|2025-08-11|August     |
|2025-01-01|January    |
+----------+-----------+
```

---

## 🎯 Example 3: Conditional Logic

```python
data = [(100,), (250,), (400,)]
df = spark.createDataFrame(data, ["sales"])

result = df.withColumn(
    "category",
    F.expr("CASE WHEN sales < 200 THEN 'Low' " +
           "WHEN sales < 350 THEN 'Medium' " +
           "ELSE 'High' END")
)

result.show()
```

**Output:**

```
+-----+--------+
|sales|category|
+-----+--------+
|100  |Low     |
|250  |Medium  |
|400  |High    |
+-----+--------+
```

---

## 🖼 Visual Representation

**Without `expr`:**

```python
df.withColumn("double_value", df["value"] * 2)
```

**With `expr`:**

```python
df.withColumn("double_value", F.expr("value * 2"))
```

---

## 🔍 Key Points

* `expr` is useful for **quick SQL-style expressions** without switching to full SQL queries.
* Supports **all Spark SQL functions** (like `date_format`, `concat_ws`, `CASE WHEN`, etc.).
* Can be combined with column references and literals.

---

