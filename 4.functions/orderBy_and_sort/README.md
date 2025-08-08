# 📊 PySpark `orderBy()` vs `sort()`

---
In PySpark, both **`orderBy()`** and **`sort()`** are used to sort the rows of a DataFrame.  
They are **functionally equivalent**, but there are slight differences in usage preference.

---

## 🛠 Syntax

```python
# orderBy
DataFrame.orderBy(*cols, **kwargs)

# sort
DataFrame.sort(*cols, **kwargs)
````

| Parameter   | Description                                               |
| ----------- | --------------------------------------------------------- |
| `*cols`     | Column(s) to sort by. Can be `Column` objects or strings. |
| `ascending` | Boolean or list of booleans. Default `True`.              |
| `kwargs`    | Named arguments like `ascending=False`.                   |

---

## 🔍 Key Points

* **`orderBy()`** is more commonly used in production code for **explicit sorting**.
* **`sort()`** is an alias for `orderBy()`, and is often preferred for **quick sorting**.
* Both support **ascending** and **descending** sorting.
* Sorting is a **wide transformation** (can trigger a shuffle in the cluster).

---

## 📌 Example 1: Basic Ascending Sort

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("OrderBySortExample").getOrCreate()

data = [("John", 25), ("Mike", 30), ("Sara", 22)]
df = spark.createDataFrame(data, ["name", "age"])

df.orderBy("age").show()
df.sort("age").show()  # Same as orderBy
```

---

## 📌 Example 2: Descending Sort

```python
df.orderBy(F.col("age").desc()).show()
df.sort(F.col("age").desc()).show()
```

---

## 📌 Example 3: Multi-column Sort

```python
df.orderBy(F.col("age").asc(), F.col("name").desc()).show()
df.sort(["age", "name"], ascending=[True, False]).show()
```

---

## 📌 Example 4: Using `ascending` Parameter

```python
df.orderBy("age", ascending=False).show()
df.sort("age", ascending=False).show()
```

---

## ⚡ Performance Tip

* Avoid unnecessary sorting in large datasets unless needed, as it can be expensive.
* For partial ordering within groups, use `partitionBy` with `Window` functions instead of full sorting.

---

## 📌 Summary Table

| Feature         | `orderBy()`                            | `sort()`                          |
| --------------- | -------------------------------------- | --------------------------------- |
| Purpose         | Sort DataFrame rows                    | Sort DataFrame rows               |
| Syntax Style    | More explicit, preferred in production | Shorter alias                     |
| Parameters      | Same as `sort()`                       | Same as `orderBy()`               |
| Performance     | Same                                   | Same                              |
| Common Use Case | Explicit ordering in pipelines         | Quick sorting in interactive work |

---
