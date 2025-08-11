# 💡 `lit` in PySpark

---

## 📝 Overview
The `lit` function in PySpark is used to **add a constant (literal) value** to a DataFrame column.  
It is commonly used when:
- You need to create a new column with the same value for all rows.
- You want to compare a column with a constant value in conditions.

**Import Path**
```python
from pyspark.sql import functions as F
````

---

## 🛠 Syntax

```python
lit(value)
```

| Parameter | Description                                                                             |
| --------- | --------------------------------------------------------------------------------------- |
| `value`   | **Required**. The constant value to be used. Can be string, number, boolean, date, etc. |

**Return Type:**
Column (constant value for each row).

---

## 🎯 Example 1: Add a Constant Column

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("LitExample").getOrCreate()

data = [("Alice", 25), ("Bob", 30)]
df = spark.createDataFrame(data, ["name", "age"])

result = df.withColumn("country", F.lit("India"))

result.show()
```

**Output:**

```
+-----+---+-------+
|name |age|country|
+-----+---+-------+
|Alice|25 |India  |
|Bob  |30 |India  |
+-----+---+-------+
```

---

## 🎯 Example 2: Conditional with `lit`

```python
result = df.withColumn(
    "is_adult",
    F.when(df.age >= F.lit(18), F.lit(True)).otherwise(F.lit(False))
)

result.show()
```

**Output:**

```
+-----+---+--------+
|name |age|is_adult|
+-----+---+--------+
|Alice|25 |true    |
|Bob  |30 |true    |
+-----+---+--------+
```

---

## 🎯 Example 3: Adding Numbers with `lit`

```python
result = df.withColumn("age_plus_5", df.age + F.lit(5))
result.show()
```

**Output:**

```
+-----+---+-----------+
|name |age|age_plus_5 |
+-----+---+-----------+
|Alice|25 |30         |
|Bob  |30 |35         |
+-----+---+-----------+
```

---

## 🖼 Visual Representation

| **Before** | **After Adding `lit` Column** |       |     |         |
| ---------- | ----------------------------- | ----- | --- | ------- |
| name       | age                           | name  | age | country |
| Alice      | 25                            | Alice | 25  | India   |
| Bob        | 30                            | Bob   | 30  | India   |

---

## 🔍 Key Points

* `lit` **wraps constants** so they can be used in DataFrame expressions.
* Supports **any data type**.
* Frequently used with:

    * `withColumn` (adding constant values)
    * `when` / `otherwise` conditions
    * Mathematical operations with columns

---

