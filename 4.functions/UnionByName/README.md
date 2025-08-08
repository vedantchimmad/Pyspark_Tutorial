# 📌 PySpark — `unionByName()`

---

## 🔹 Overview
In PySpark, **`unionByName()`** is used to combine **two DataFrames based on column names**, not column positions.  
This is useful when:
- DataFrames have **same column names but different order**.
- DataFrames have **different column sets** (extra/missing columns).

💡 Optional parameter **`allowMissingColumns`** allows you to union DataFrames even if one DataFrame has extra columns.  
Missing columns will be filled with **`null`** values.

---

## 🔹 Syntax
```python
DataFrame1.unionByName(DataFrame2, allowMissingColumns=False)
````

| Parameter               | Description                                                                                                          |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **DataFrame2**          | Another DataFrame to union with.                                                                                     |
| **allowMissingColumns** | Default `False`. If `True`, allows union of DataFrames with different columns by filling missing columns with nulls. |

---

## 🔹 Example 1 — Same Columns, Different Order

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("UnionByNameExample").getOrCreate()

data1 = [("Alice", 25)]
data2 = [(30, "Bob")]

columns1 = ["Name", "Age"]
columns2 = ["Age", "Name"]

df1 = spark.createDataFrame(data1, columns1)
df2 = spark.createDataFrame(data2, columns2)

# Union by column name
df_union = df1.unionByName(df2)
df_union.show()
```

**Output**

```
+-----+---+
| Name|Age|
+-----+---+
|Alice| 25|
|  Bob| 30|
+-----+---+
```

✅ Column order differences handled automatically.

---

## 🔹 Example 2 — Different Number of Columns

```python
data1 = [("Alice", 25)]
data2 = [("Bob", 30, "NY")]

columns1 = ["Name", "Age"]
columns2 = ["Name", "Age", "City"]

df1 = spark.createDataFrame(data1, columns1)
df2 = spark.createDataFrame(data2, columns2)

# Allow missing columns → fills with nulls
df_union = df1.unionByName(df2, allowMissingColumns=True)
df_union.show()
```

**Output**

```
+-----+---+----+
| Name|Age|City|
+-----+---+----+
|Alice| 25|null|
|  Bob| 30|  NY|
+-----+---+----+
```

✅ Missing `City` column in `df1` filled with `null`.

---

## 🔹 SQL Equivalent

There is **no direct SQL equivalent** of `unionByName()` because SQL unions are **position-based**, not **name-based**.
In SQL, you must **manually align column orders**.

---

## 🔹 Key Points

| Feature                    | `union()`        | `unionByName()`                    |
| -------------------------- | ---------------- | ---------------------------------- |
| Match Based On             | Column position  | Column name                        |
| Handles Different Order    | ❌ No             | ✅ Yes                              |
| Handles Missing Columns    | ❌ No             | ✅ Yes (`allowMissingColumns=True`) |
| Default Duplicate Handling | Keeps duplicates | Keeps duplicates                   |

---

✅ **Summary:**
Use `unionByName()` when:

* Column **order differs**.
* You want **name-based matching**.
* You need to **handle missing columns gracefully** with `allowMissingColumns=True`.

