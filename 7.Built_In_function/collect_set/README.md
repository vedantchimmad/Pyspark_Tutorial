# 📌 `collect_set` in PySpark

---

## 📝 Overview
`collect_set` is an **aggregate function** in PySpark that returns a **set of unique values** for each group, **removing duplicates**.  
It’s useful when you want distinct values collected into an array per group.

**Import Path**
```python
from pyspark.sql import functions as F
````

---

## 🛠 Syntax

```python
collect_set(column)
```

| Parameter | Description                                                        |
| --------- | ------------------------------------------------------------------ |
| `column`  | The column whose distinct values need to be collected into a list. |

---

## 🎯 Example: Using `collect_set`

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Create SparkSession
spark = SparkSession.builder.appName("CollectSetExample").getOrCreate()

# Sample Data
data = [
    ("A", 10),
    ("A", 20),
    ("B", 30),
    ("B", 40),
    ("A", 10)  # duplicate
]

# Create DataFrame
df = spark.createDataFrame(data, ["category", "value"])

# Using collect_set
result = df.groupBy("category").agg(F.collect_set("value").alias("unique_values"))

result.show(truncate=False)
```

**Output:**

```
+--------+-------------+
|category|unique_values|
+--------+-------------+
|A       |[10, 20]     |
|B       |[30, 40]     |
+--------+-------------+
```

---

## 🔍 Difference Between `collect_list` and `collect_set`

| Function       | Duplicates Kept? | Order Guaranteed? |
| -------------- | ---------------- | ----------------- |
| `collect_list` | ✅ Yes            | ❌ No              |
| `collect_set`  | ❌ No             | ❌ No              |

---

## 🖼 Visual Representation

```
Category A → {10, 20}
Category B → {30, 40}

          collect_set
   ┌────────────────────────────┐
   | Group data by "category"   |
   | Gather unique "value"      |
   | Return as array (set-like) |
   └────────────────────────────┘
```

---

## 🔗 Notes

* `collect_set` **removes duplicates** automatically.
* Does **not** preserve element order.
* Use `sort_array()` if you want results in a sorted list.

```python
# Example: Sorted set
df.groupBy("category") \
  .agg(F.sort_array(F.collect_set("value")).alias("sorted_unique")) \
  .show()
```

