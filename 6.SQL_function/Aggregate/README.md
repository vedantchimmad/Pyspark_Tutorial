# 📊 PySpark Aggregate Functions

---

In PySpark, **aggregation functions** help summarize or compute statistics on data.  
They are often used with **`groupBy()`**, **`agg()`**, or **`select()`**.

---

## 🔹 **Common Aggregate Functions**

| 🛠 Function | 📖 Description |
|-------------|---------------|
| `count()` | 🔢 Count number of rows |
| `sum()` | ➕ Sum of values |
| `avg()` | 📏 Average value |
| `max()` | 🔼 Maximum value |
| `min()` | 🔽 Minimum value |
| `first()` | 🎯 First value |
| `last()` | 🎯 Last value |
| `collect_list()` | 📝 All values as a list (with duplicates) |
| `collect_set()` | 📝 All unique values as a set |

---

## 📝 **Syntax**
```python
from pyspark.sql import functions as F

df.groupBy(column_names).agg(aggregation_expressions)
````

---

## 📂 **Sample Data**

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("Aggregate Example").getOrCreate()

data = [
    ("James", "Sales", 3000),
    ("Michael", "Sales", 4600),
    ("Robert", "Sales", 4100),
    ("Maria", "Finance", 3000),
    ("Raman", "Finance", 3000),
    ("Scott", "Finance", 3300),
    ("Jen", "Finance", 3900),
    ("Jeff", "Marketing", 3000),
    ("Kumar", "Marketing", 2000)
]
columns = ["name", "dept", "salary"]

df = spark.createDataFrame(data, columns)
```

---

## 1️⃣ **Group By with Single Aggregation**

```python
df.groupBy("dept").agg(
    F.sum("salary").alias("💰 total_salary")
).show()
```

---

## 2️⃣ **Group By with Multiple Aggregations**

```python
df.groupBy("dept").agg(
    F.sum("salary").alias("💰 total_salary"),
    F.avg("salary").alias("📏 avg_salary"),
    F.max("salary").alias("🔼 max_salary"),
    F.min("salary").alias("🔽 min_salary"),
    F.count("salary").alias("👥 employee_count")
).show()
```

---

## 3️⃣ **Global Aggregation (Without Grouping)**

```python
df.agg(
    F.sum("salary").alias("💰 total_salary"),
    F.avg("salary").alias("📏 avg_salary")
).show()
```

---

## 4️⃣ **Count Distinct Values**

```python
df.groupBy("dept").agg(
    F.countDistinct("salary").alias("🔢 distinct_salaries")
).show()
```

---

## 5️⃣ **Collect List & Set**

```python
df.groupBy("dept").agg(
    F.collect_list("name").alias("📝 employee_list"),
    F.collect_set("name").alias("🗂 unique_employee_set")
).show(truncate=False)
```

---

## 6️⃣ **Multiple Columns in Group By**

```python
df.groupBy("dept", "salary").count().show()
```

---

💡 **Notes:**

* **`groupBy()`** groups rows with the same value in one or more columns.
* **`agg()`** can run multiple aggregation functions in one call.
* Use **`select()`** for aggregation without grouping (returns a single row unless a group is specified).

```

I can also prepare a **single compact table output** showing sum, avg, min, max, and count for each department side-by-side with icons, so it’s visually easy to compare.
```
