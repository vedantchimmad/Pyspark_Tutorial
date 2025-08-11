# 📅 `to_date` in PySpark

---

## 📝 Overview
The `to_date` function in PySpark converts a **string** or **timestamp** to a `DateType` column using an optional format.

**Import Path**
```python
from pyspark.sql.functions import to_date
````

---

## 🛠 Syntax

```python
to_date(col, format=None)
```

| Parameter | Description                                                                                                        |
| --------- | ------------------------------------------------------------------------------------------------------------------ |
| `col`     | **Required**. Column name or expression with date/timestamp string.                                                |
| `format`  | **Optional**. Date format string (Java `SimpleDateFormat` style). If omitted, Spark uses the default `yyyy-MM-dd`. |

**Return Type:**
`DateType`

---

## 📌 Supported Format Examples

| Format String | Meaning           | Example    |
| ------------- | ----------------- | ---------- |
| `yyyy-MM-dd`  | Year-Month-Day    | 2025-08-11 |
| `dd/MM/yyyy`  | Day/Month/Year    | 11/08/2025 |
| `MM-dd-yyyy`  | Month-Day-Year    | 08-11-2025 |
| `yyyyMMdd`    | Continuous digits | 20250811   |

---

## ⚠ Important Notes

* If the string doesn't match the given format, the result will be `null`.
* `to_date` drops the time part from timestamps — use `to_timestamp` if you need time too.
* Parsing is case-sensitive for month/day abbreviations (e.g., `MMM` vs `mmm`).

---

## 🎯 Example 1: Default Format

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date

spark = SparkSession.builder.appName("ToDateExample").getOrCreate()

data = [("2025-08-11",), ("2024-12-31",)]
df = spark.createDataFrame(data, ["date_str"])

df = df.withColumn("date_val", to_date("date_str"))

df.show()
```

**Output:**

```
+----------+----------+
| date_str | date_val |
+----------+----------+
|2025-08-11|2025-08-11|
|2024-12-31|2024-12-31|
+----------+----------+
```

---

## 🎯 Example 2: Custom Format

```python
data = [("11/08/2025",), ("31/12/2024",)]
df = spark.createDataFrame(data, ["date_str"])

df = df.withColumn("date_val", to_date("date_str", "dd/MM/yyyy"))

df.show()
```

**Output:**

```
+----------+----------+
| date_str | date_val |
+----------+----------+
|11/08/2025|2025-08-11|
|31/12/2024|2024-12-31|
+----------+----------+
```

---

## 🎯 Example 3: From Timestamp

```python
data = [("2025-08-11 14:45:30",)]
df = spark.createDataFrame(data, ["ts_str"])

df = df.withColumn("date_val", to_date("ts_str"))

df.show()
```

**Output:**

```
+-------------------+----------+
| ts_str            | date_val |
+-------------------+----------+
|2025-08-11 14:45:30|2025-08-11|
+-------------------+----------+
```

---

## 🎯 Example 4: Invalid Format → Null

```python
data = [("08-11-2025",)]
df = spark.createDataFrame(data, ["date_str"])

df = df.withColumn("date_val", to_date("date_str", "yyyy-MM-dd"))

df.show()
```

**Output:**

```
+----------+--------+
| date_str |date_val|
+----------+--------+
|08-11-2025|    null|
+----------+--------+
```

---

## 🔍 Key Points

* Always match your format string with the actual data format.
* Use `to_timestamp` if you also need **hours, minutes, and seconds**.
* Null values often mean **format mismatch** or **invalid date**.

---

