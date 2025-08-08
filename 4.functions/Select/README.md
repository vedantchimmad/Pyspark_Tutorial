# 📌 PySpark `select()` Function

---

## 🔹 Overview
In PySpark, the **`select()`** function is used to project (choose) specific columns or perform expressions on columns in a **DataFrame**.  
It is similar to the **SELECT** statement in SQL.

---

## 🔹 Syntax
```python
DataFrame.select(*cols)
````

| Parameter | Description                                                        |
| --------- | ------------------------------------------------------------------ |
| **cols**  | Column names (as strings) or `Column` expressions using functions. |

---

## 🔹 Example 1 — Selecting Specific Columns

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SelectExample").getOrCreate()

data = [("Alice", 25, "HR"), ("Bob", 30, "IT"), ("Cathy", 28, "Finance")]
columns = ["Name", "Age", "Dept"]

df = spark.createDataFrame(data, columns)

# Select specific columns
df.select("Name", "Age").show()
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

## 🔹 Example 2 — Selecting with Column Expressions

```python
from pyspark.sql.functions import col, upper

# Select with expressions
df.select(col("Name"), (col("Age") + 5).alias("Age_plus_5")).show()

# Using built-in functions
df.select(upper(col("Dept")).alias("Department_Upper")).show()
```

---

## 🔹 Example 3 — Using SQL Query Style

```python
df.createOrReplaceTempView("employees")
spark.sql("SELECT Name, Age FROM employees").show()
```

---

## 🔹 Key Points

| Feature                     | Description                                    |
| --------------------------- | ---------------------------------------------- |
| **Select by column name**   | `df.select("col1", "col2")`                    |
| **Select using `col()`**    | `df.select(col("col1"))`                       |
| **Select with expressions** | `df.select((col("col1")+10).alias("newCol"))`  |
| **Select all columns**      | `df.select("*")`                               |
| **SQL style**               | Using `spark.sql()` after creating a temp view |

---

✅ **Summary:**

* `select()` is **column projection**.
* Supports both **direct column names** and **expressions**.
* Can be combined with **PySpark functions** for transformations.

