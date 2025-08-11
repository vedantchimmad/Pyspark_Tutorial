# 📅 `datediff` in PySpark

---

## 📝 Overview
The `datediff` function calculates the **number of days** between two date/timestamp columns.

**Import Path**
```python
from pyspark.sql import functions as F
````

---

## 🛠 Syntax

```python
datediff(end_date, start_date)
```

| Parameter    | Description                                                              |
| ------------ | ------------------------------------------------------------------------ |
| `end_date`   | **Required**. Column or expression with a date/timestamp (later date).   |
| `start_date` | **Required**. Column or expression with a date/timestamp (earlier date). |

**Return Type:** `Integer` (positive, negative, or zero depending on date order)

---

## 🎯 Example 1: Difference Between Two Dates

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Create SparkSession
spark = SparkSession.builder.appName("DateDiffExample").getOrCreate()

# Sample Data
data = [("2025-08-11", "2025-08-01"),
        ("2025-08-01", "2025-08-11"),
        ("2025-08-11", "2025-08-11")]

df = spark.createDataFrame(data, ["end_date_str", "start_date_str"])

# Convert to Date Type
df = df.withColumn("end_date", F.to_date("end_date_str")) \
       .withColumn("start_date", F.to_date("start_date_str"))

# Calculate date difference
result = df.withColumn("days_diff", F.datediff("end_date", "start_date"))

result.show()
```

**Output:**

```
+-------------+--------------+----------+----------+---------+
|end_date_str |start_date_str|end_date  |start_date|days_diff|
+-------------+--------------+----------+----------+---------+
|2025-08-11   |2025-08-01    |2025-08-11|2025-08-01|10       |
|2025-08-01   |2025-08-11    |2025-08-01|2025-08-11|-10      |
|2025-08-11   |2025-08-11    |2025-08-11|2025-08-11|0        |
+-------------+--------------+----------+----------+---------+
```

---

## 🎯 Example 2: Calculate Age in Days

```python
birthdays = [("John", "1995-06-15"),
             ("Emma", "2000-01-01")]

df_birth = spark.createDataFrame(birthdays, ["name", "dob_str"])

df_birth = df_birth.withColumn("dob", F.to_date("dob_str"))

age_days = df_birth.withColumn(
    "age_in_days",
    F.datediff(F.current_date(), "dob")
)

age_days.show()
```

**Output (example):**

```
+----+----------+----------+-----------+
|name|dob_str   |dob       |age_in_days|
+----+----------+----------+-----------+
|John|1995-06-15|1995-06-15|11036      |
|Emma|2000-01-01|2000-01-01| 9355      |
+----+----------+----------+-----------+
```

---

## 🖼 Visual Representation

```
start_date: 2025-08-01
end_date:   2025-08-11

datediff = end_date - start_date = 10 days
```

---

## 🔍 Key Points

* **Order matters**: `datediff(end, start)` returns positive if `end` > `start`, negative if reversed.
* Works with both `date` and `timestamp` columns (timestamps are truncated to date before calculation).
* Returns integer count of days, **time portion is ignored**.


