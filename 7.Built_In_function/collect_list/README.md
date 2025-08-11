# 📌 `collect_list` in PySpark

---

## 📝 Overview
`collect_list` is an **aggregate function** in PySpark that returns a **list of values** for each group without removing duplicates.  
It’s useful when you want to gather all values of a column into an array per group.

**Import Path**
```python
from pyspark.sql import functions as F
````

---

## 🛠 Syntax

```python
collect_list(column)
```

| Parameter | Description                                               |
| --------- | --------------------------------------------------------- |
| `column`  | The column whose values need to be collected into a list. |

---

## 🎯 Example: Using `collect_list`

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Create SparkSession
spark = SparkSession.builder.appName("CollectListExample").getOrCreate()

# Sample Data
data = [
    ("A", 10),
    ("A", 20),
    ("B", 30),
    ("B", 40),
    ("A", 10)  # duplicate to show difference with collect_set
]

# Create DataFrame
df = spark.createDataFrame(data, ["category", "value"])

# Using collect_list
result = df.groupBy("category").agg(F.collect_list("value").alias("values_list"))

result.show(truncate=False)
```

**Output:**

```
+--------+-------------+
|category|values_list  |
+--------+-------------+
|A       |[10, 20, 10] |
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
Category A → [10, 20, 10]
Category B → [30, 40]

          collect_list
   ┌────────────────────────────┐
   | Group data by "category"   |
   | Gather all "value" entries |
   | Return as array            |
   └────────────────────────────┘
```

---

## 🔗 Notes

* `collect_list` **does not guarantee order** in the result array.
* Use `sort_array()` if you want the list sorted.
* Works only as an **aggregation** inside `groupBy` or `agg`.

```python
# Example: Sorted list
df.groupBy("category") \
  .agg(F.sort_array(F.collect_list("value")).alias("sorted_list")) \
  .show()
```

