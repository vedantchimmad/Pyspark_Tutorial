# 📅 `date_format` in PySpark

---

## 📝 Overview
The `date_format` function formats a **date/timestamp column** into a **string** based on a specified date/time pattern.

**Import Path**
```python
from pyspark.sql import functions as F
````

---

## 🛠 Syntax

```python
date_format(date_col, format)
```

| Parameter  | Description                                                               |
| ---------- | ------------------------------------------------------------------------- |
| `date_col` | **Required**. The column containing date or timestamp values.             |
| `format`   | **Required**. The date/time pattern string (Java SimpleDateFormat style). |

---

## 📌 Common Format Patterns

| Pattern | Description             | Example Output |
| ------- | ----------------------- | -------------- |
| `yyyy`  | Year (4 digits)         | 2025           |
| `yy`    | Year (2 digits)         | 25             |
| `MM`    | Month (2 digits)        | 08             |
| `MMM`   | Abbreviated month name  | Aug            |
| `MMMM`  | Full month name         | August         |
| `dd`    | Day of month (2 digits) | 11             |
| `EEE`   | Abbreviated day name    | Mon            |
| `EEEE`  | Full day name           | Monday         |
| `HH`    | Hour (00–23)            | 17             |
| `hh`    | Hour (01–12)            | 05             |
| `mm`    | Minutes                 | 07             |
| `ss`    | Seconds                 | 45             |
| `a`     | AM/PM marker            | PM             |

---

## 🎯 Example 1: Format a Timestamp

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Create SparkSession
spark = SparkSession.builder.appName("DateFormatExample").getOrCreate()

# Sample Data
data = [("2025-08-11 17:30:45",)]
df = spark.createDataFrame(data, ["timestamp_str"])

# Convert string to timestamp
df = df.withColumn("timestamp", F.to_timestamp("timestamp_str"))

# Format timestamp
result = df.withColumn(
    "formatted_date",
    F.date_format("timestamp", "dd-MMM-yyyy HH:mm:ss")
)

result.show(truncate=False)
```

**Output:**

```
+-------------------+-------------------+-------------------+
|timestamp_str      |timestamp          |formatted_date     |
+-------------------+-------------------+-------------------+
|2025-08-11 17:30:45|2025-08-11 17:30:45|11-Aug-2025 17:30:45|
+-------------------+-------------------+-------------------+
```

---

## 🎯 Example 2: Extract Specific Parts of Date

```python
df_parts = df.withColumn("year", F.date_format("timestamp", "yyyy")) \
             .withColumn("month_name", F.date_format("timestamp", "MMMM")) \
             .withColumn("day_name", F.date_format("timestamp", "EEEE"))

df_parts.show(truncate=False)
```

**Output:**

```
+-------------------+-------------------+----+----------+---------+
|timestamp_str      |timestamp          |year|month_name|day_name |
+-------------------+-------------------+----+----------+---------+
|2025-08-11 17:30:45|2025-08-11 17:30:45|2025|August    |Monday   |
+-------------------+-------------------+----+----------+---------+
```

---

## 🖼 Visual Representation

```
[2025-08-11 17:30:45]
        ↓ date_format("dd-MMM-yyyy HH:mm:ss")
"11-Aug-2025 17:30:45"
```

---

## 🔍 Key Points

* Uses Java’s `SimpleDateFormat` patterns.
* Always returns a **string** column.
* Useful for **display formatting** and **extracting parts of date**.

