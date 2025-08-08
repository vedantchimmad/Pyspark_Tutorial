# 📌 PySpark — `withColumn()`

---

## 🔹 Overview
In PySpark, **`withColumn()`** is used to **create a new column** or **replace an existing column** in a DataFrame.  
It takes:
- The **column name** (string).
- A **Column expression** (PySpark Column object, not just a Python value).

---

## 🔹 Syntax
```python
DataFrame.withColumn(colName, colExpression)
````

| Parameter         | Description                                                           |
| ----------------- | --------------------------------------------------------------------- |
| **colName**       | Name of the column to create or replace.                              |
| **colExpression** | A PySpark **Column** object representing the transformation or value. |

---

## 🔹 Example 1 — Add New Column

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("WithColumnExample").getOrCreate()

data = [("Alice", 25), ("Bob", 30)]
columns = ["Name", "Age"]

df = spark.createDataFrame(data, columns)

# Add a new column "Age_10" = Age + 10
df_new = df.withColumn("Age_10", col("Age") + 10)
df_new.show()
```

**Output**

```
+-----+---+------+
| Name|Age|Age_10|
+-----+---+------+
|Alice| 25|    35|
|  Bob| 30|    40|
+-----+---+------+
```

---

## 🔹 Example 2 — Replace Existing Column

```python
# Replace "Age" column with Age * 2
df_replace = df.withColumn("Age", col("Age") * 2)
df_replace.show()
```

**Output**

```
+-----+---+
| Name|Age|
+-----+---+
|Alice| 50|
|  Bob| 60|
+-----+---+
```

---

## 🔹 Example 3 — Create Column Using Built-in Functions

```python
from pyspark.sql.functions import lit, upper

# Add constant column & uppercase name
df_func = df.withColumn("Country", lit("USA")) \
            .withColumn("Name_Upper", upper(col("Name")))
df_func.show()
```

**Output**

```
+-----+---+-------+----------+
| Name|Age|Country|Name_Upper|
+-----+---+-------+----------+
|Alice| 25|    USA|     ALICE|
|  Bob| 30|    USA|       BOB|
+-----+---+-------+----------+
```

---

## 🔹 Example 4 — Conditional Column

```python
from pyspark.sql.functions import when

# Categorize age
df_cond = df.withColumn(
    "Age_Group",
    when(col("Age") < 30, "Young").otherwise("Adult")
)
df_cond.show()
```

**Output**

```
+-----+---+---------+
| Name|Age|Age_Group|
+-----+---+---------+
|Alice| 25|    Young|
|  Bob| 30|    Adult|
+-----+---+---------+
```

---

## 🔹 Notes & Best Practices

1. **Overwrites column if it already exists.**
2. **Column expression must be a PySpark Column object** — use `col()`, `lit()`, `when()`, etc.
3. For adding **multiple columns**, chain multiple `.withColumn()` calls.
4. For performance, avoid excessive `.withColumn()` chaining — consider using `.select()` for multiple transformations in one step.

---

✅ **Summary:**
`withColumn()` is your go-to function for **adding or replacing columns** in a PySpark DataFrame, supporting transformations, constants, and conditional logic.
