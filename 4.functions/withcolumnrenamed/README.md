# 📌 PySpark — `withColumnRenamed()`

---

## 🔹 Overview
In PySpark, **`withColumnRenamed()`** is used to **rename an existing column** in a DataFrame.  
It takes:
- The **current column name**.
- The **new column name**.

---

## 🔹 Syntax
```python
DataFrame.withColumnRenamed(existing, new)
````

| Parameter    | Description                                     |
| ------------ | ----------------------------------------------- |
| **existing** | Name of the column you want to rename (string). |
| **new**      | New name for the column (string).               |

---

## 🔹 Example 1 — Rename Single Column

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("WithColumnRenamedExample").getOrCreate()

data = [("Alice", 25), ("Bob", 30)]
columns = ["Name", "Age"]

df = spark.createDataFrame(data, columns)

# Rename "Age" to "Years"
df_renamed = df.withColumnRenamed("Age", "Years")
df_renamed.show()
```

**Output**

```
+-----+-----+
| Name|Years|
+-----+-----+
|Alice|   25|
|  Bob|   30|
+-----+-----+
```

---

## 🔹 Example 2 — Rename Multiple Columns (Chaining)

```python
df_multi = df.withColumnRenamed("Name", "Full_Name") \
             .withColumnRenamed("Age", "Age_in_Years")
df_multi.show()
```

**Output**

```
+---------+-------------+
|Full_Name|Age_in_Years |
+---------+-------------+
|    Alice|           25|
|      Bob|           30|
+---------+-------------+
```

---

## 🔹 Example 3 — Rename Columns Dynamically

```python
# Using reduce to rename multiple columns dynamically
from functools import reduce

new_names = {"Name": "Employee_Name", "Age": "Employee_Age"}

df_dynamic = reduce(
    lambda df, col: df.withColumnRenamed(col, new_names[col]),
    new_names,
    df
)
df_dynamic.show()
```

**Output**

```
+-------------+------------+
|Employee_Name|Employee_Age|
+-------------+------------+
|        Alice|          25|
|          Bob|          30|
+-------------+------------+
```

---

## 🔹 Notes & Best Practices

1. **Case-sensitive** — `"age"` and `"Age"` are different.
2. Cannot rename **multiple columns in one method call** — must chain or loop.
3. When working with **many columns**, prefer `toDF()` for renaming all at once:

   ```python
   df.toDF("Full_Name", "Years")
   ```
4. Does not modify the original DataFrame — returns a **new DataFrame**.

---

✅ **Summary:**
`withColumnRenamed()` is the simplest way to **rename a single column** in PySpark.
For multiple renames, chain calls or use a loop/dynamic approach.

