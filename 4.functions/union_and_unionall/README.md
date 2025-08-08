# 📌 PySpark — `union()` & `unionAll()`

---

## 🔹 Overview
In PySpark, **`union()`** and **`unionAll()`** are used to combine **two DataFrames with the same schema** (same number of columns and same column names & data types).

💡 **Difference:**
- **`union()`** → Removes duplicate rows (like SQL `UNION`).
- **`unionAll()`** → Keeps all rows, including duplicates (like SQL `UNION ALL`).

⚠️ **Note:** In Spark 2.0+, `unionAll()` was deprecated and replaced by `union()` (which works like `UNION ALL`).  
If you want duplicate removal, use `union().distinct()`.

---

## 🔹 Syntax
```python
DataFrame1.union(DataFrame2)
DataFrame1.unionAll(DataFrame2)   # Deprecated
````

| Parameter      | Description                                           |
| -------------- | ----------------------------------------------------- |
| **DataFrame2** | Another DataFrame with the same schema as DataFrame1. |

---

## 🔹 Example — `union()` (with duplicate removal)

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("UnionExample").getOrCreate()

data1 = [("Alice", 25), ("Bob", 30)]
data2 = [("Cathy", 28), ("Bob", 30)]

columns = ["Name", "Age"]

df1 = spark.createDataFrame(data1, columns)
df2 = spark.createDataFrame(data2, columns)

# UNION (remove duplicates)
df_union = df1.union(df2).distinct()
df_union.show()
```

**Output**

```
+-----+---+
| Name|Age|
+-----+---+
|Alice| 25|
|  Bob| 30|
|Cathy| 28|
+-----+---+
```

---

## 🔹 Example — `unionAll()` / `union()` without distinct

```python
# UNION ALL (keeps duplicates)
df_union_all = df1.union(df2)  # behaves like unionAll in Spark 2.x+
df_union_all.show()
```

**Output**

```
+-----+---+
| Name|Age|
+-----+---+
|Alice| 25|
|  Bob| 30|
|Cathy| 28|
|  Bob| 30|
+-----+---+
```

---

## 🔹 Example — SQL Equivalent

```python
df1.createOrReplaceTempView("table1")
df2.createOrReplaceTempView("table2")

# UNION (remove duplicates)
spark.sql("SELECT * FROM table1 UNION SELECT * FROM table2").show()

# UNION ALL (keep duplicates)
spark.sql("SELECT * FROM table1 UNION ALL SELECT * FROM table2").show()
```

---

## 🔹 Key Points

| Feature                   | `union()`                             | `unionAll()`                  |
| ------------------------- | ------------------------------------- | ----------------------------- |
| Duplicates Removed?       | ✅ Yes (if `.distinct()` used)         | ❌ No                          |
| Deprecated?               | No                                    | ✅ Yes (use `union()` instead) |
| Schema Matching Required? | ✅ Yes                                 | ✅ Yes                         |
| Performance               | Slightly slower if `.distinct()` used | Faster (no duplicate removal) |

---

✅ **Summary:**

* Use `union()` in Spark 2.x+ for **both** `UNION` and `UNION ALL` behavior.
* To remove duplicates → `df1.union(df2).distinct()`
* To keep duplicates → `df1.union(df2)` (default behavior).

