# 📊 PySpark `groupBy()` Function

---
The `groupBy()` function in PySpark is used to **group data** in a DataFrame based on one or more columns.  
It is similar to the SQL `GROUP BY` statement and is often followed by **aggregation functions** such as `count()`, `sum()`, `avg()`, `max()`, etc.

---

## 🛠 Syntax

```python
DataFrame.groupBy(*cols)
````

| Parameter | Description                                                |
| --------- | ---------------------------------------------------------- |
| `*cols`   | One or more column names or expressions to group the data. |

---

## ⚡ Key Points

* Returns a **GroupedData** object.
* Needs an **aggregation** to get meaningful results.
* Can group by **one or multiple columns**.
* Works similar to `GROUP BY` in SQL.

---

## 📌 Example 1: Group by Single Column

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("GroupByExample").getOrCreate()

data = [("Alice", "Math", 85),
        ("Bob", "Math", 70),
        ("Alice", "English", 95),
        ("Bob", "English", 80)]

df = spark.createDataFrame(data, ["name", "subject", "score"])

df.groupBy("name").agg(F.avg("score").alias("avg_score")).show()
```

**Output**

```
+-----+---------+
| name|avg_score|
+-----+---------+
|Alice|     90.0|
|  Bob|     75.0|
+-----+---------+
```

---

## 📌 Example 2: Group by Multiple Columns

```python
df.groupBy("name", "subject").agg(F.max("score").alias("max_score")).show()
```

**Output**

```
+-----+-------+---------+
| name|subject|max_score|
+-----+-------+---------+
|Alice|   Math|       85|
|Alice|English|       95|
|  Bob|   Math|       70|
|  Bob|English|       80|
+-----+-------+---------+
```

---

## 📌 Example 3: Multiple Aggregations

```python
df.groupBy("name").agg(
    F.avg("score").alias("avg_score"),
    F.min("score").alias("min_score"),
    F.max("score").alias("max_score")
).show()
```

---

## 📌 Example 4: Group by with Filter (HAVING Equivalent)

```python
df.groupBy("name").agg(F.avg("score").alias("avg_score")) \
  .filter(F.col("avg_score") > 80) \
  .show()
```

---

## 📌 Example 5: Group by with SQL

```python
df.createOrReplaceTempView("students")

spark.sql("""
SELECT name, AVG(score) as avg_score
FROM students
GROUP BY name
""").show()
```

---

## 🚀 When to Use

* Aggregating data based on categories.
* Performing statistical analysis per group.
* Implementing SQL-like `GROUP BY` in PySpark.

---

## 🛑 Common Mistakes

* Forgetting to use aggregation after `groupBy()`.
* Expecting `groupBy()` to return grouped data directly — it only returns a **GroupedData** object until you aggregate.

---

