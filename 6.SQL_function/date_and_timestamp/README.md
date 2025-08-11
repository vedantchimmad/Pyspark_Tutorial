# 📅 Date & ⏱ Timestamp Functions in PySpark

---

PySpark provides built-in functions to work with **dates** and **timestamps** for extraction, formatting, and manipulation.

---

## 🛠 **Import**
```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("Date & Timestamp").getOrCreate()
````

---

## 📂 **Sample Data**

```python
data = [("2025-08-08", "2025-08-08 15:30:45"),
        ("2024-12-25", "2024-12-25 09:15:30")]
columns = ["date_str", "timestamp_str"]

df = spark.createDataFrame(data, columns)
df = df.withColumn("date_col", F.to_date("date_str")) \
       .withColumn("timestamp_col", F.to_timestamp("timestamp_str"))

df.show(truncate=False)
```

---

## 1️⃣ **Convert String to Date/Timestamp**

```python
df.withColumn("📅 date_val", F.to_date("date_str", "yyyy-MM-dd")) \
  .withColumn("⏱ timestamp_val", F.to_timestamp("timestamp_str", "yyyy-MM-dd HH:mm:ss")) \
  .show()
```

---

## 2️⃣ **Extract Date Parts**

```python
df.select(
    "date_col",
    F.year("date_col").alias("📆 year"),
    F.month("date_col").alias("📅 month"),
    F.dayofmonth("date_col").alias("📅 day"),
    F.dayofweek("date_col").alias("📅 weekday_num"), # 1=Sunday
    F.dayofyear("date_col").alias("📅 day_of_year"),
    F.weekofyear("date_col").alias("📅 week_of_year"),
).show()
```

---

## 3️⃣ **Extract Time Parts**

```python
df.select(
    "timestamp_col",
    F.hour("timestamp_col").alias("⏰ hour"),
    F.minute("timestamp_col").alias("⏳ minute"),
    F.second("timestamp_col").alias("⏱ second")
).show()
```

---

## 4️⃣ **Date Arithmetic**

```python
df.select(
    "date_col",
    F.date_add("date_col", 5).alias("📅 plus_5_days"),
    F.date_sub("date_col", 5).alias("📅 minus_5_days"),
    F.add_months("date_col", 2).alias("📅 plus_2_months"),
    F.add_months("date_col", -2).alias("📅 minus_2_months")
).show()
```

---

## 5️⃣ **Difference Between Dates**

```python
df.select(
    "date_col",
    F.datediff(F.current_date(), "date_col").alias("📊 days_diff"),
    F.months_between(F.current_date(), "date_col").alias("📊 months_diff")
).show()
```

---

## 6️⃣ **Current Date & Timestamp**

```python
df.select(
    F.current_date().alias("📅 today"),
    F.current_timestamp().alias("⏱ now")
).show(truncate=False)
```

---

## 7️⃣ **Formatting Dates/Timestamps**

```python
df.select(
    "timestamp_col",
    F.date_format("timestamp_col", "yyyy-MM-dd HH:mm:ss").alias("📄 full_format"),
    F.date_format("timestamp_col", "MMM dd, yyyy").alias("📄 custom_format"),
    F.date_format("timestamp_col", "EEEE").alias("📄 day_name")
).show()
```

---

## 8️⃣ **Truncate Date**

```python
df.select(
    "timestamp_col",
    F.trunc("date_col", "MM").alias("📅 first_day_of_month"),
    F.date_trunc("hour", "timestamp_col").alias("⏱ truncate_to_hour")
).show()
```

---

💡 **Notes:**

* Use **`to_date()`** for date only, and **`to_timestamp()`** for date & time.
* **`date_format()`** is handy for creating human-readable formats.
* Time zones can be handled with **`from_utc_timestamp()`** and **`to_utc_timestamp()`**.

---
## 📅 Date & ⏱ Timestamp Functions in PySpark

---

Below is a **complete reference table** of commonly used **date** and **timestamp** functions in PySpark, with descriptions, syntax, and examples.

---

| 📌 Function | 📝 Description | 🖥️ Example | 🏷️ Output Example |
|-------------|---------------|------------|-------------------|
| **`current_date()`** | Returns the current system date. | `df.select(F.current_date())` | `2025-08-08` |
| **`current_timestamp()`** | Returns the current system timestamp. | `df.select(F.current_timestamp())` | `2025-08-08 15:45:10` |
| **`to_date(col, fmt)`** | Converts a string to date using an optional format. | `F.to_date("date_str", "yyyy-MM-dd")` | `2025-08-08` |
| **`to_timestamp(col, fmt)`** | Converts a string to timestamp using an optional format. | `F.to_timestamp("timestamp_str", "yyyy-MM-dd HH:mm:ss")` | `2025-08-08 15:30:45` |
| **`year(col)`** | Extracts the year from a date/timestamp. | `F.year("date_col")` | `2025` |
| **`month(col)`** | Extracts the month number (1-12). | `F.month("date_col")` | `8` |
| **`dayofmonth(col)`** | Extracts the day of the month. | `F.dayofmonth("date_col")` | `8` |
| **`dayofweek(col)`** | Returns the day of week (1=Sunday). | `F.dayofweek("date_col")` | `6` |
| **`dayofyear(col)`** | Returns the day of year (1–366). | `F.dayofyear("date_col")` | `220` |
| **`weekofyear(col)`** | Returns the week of year. | `F.weekofyear("date_col")` | `32` |
| **`hour(col)`** | Extracts the hour from a timestamp. | `F.hour("timestamp_col")` | `15` |
| **`minute(col)`** | Extracts the minute from a timestamp. | `F.minute("timestamp_col")` | `30` |
| **`second(col)`** | Extracts the seconds from a timestamp. | `F.second("timestamp_col")` | `45` |
| **`date_add(col, days)`** | Adds days to a date. | `F.date_add("date_col", 5)` | `2025-08-13` |
| **`date_sub(col, days)`** | Subtracts days from a date. | `F.date_sub("date_col", 5)` | `2025-08-03` |
| **`add_months(col, months)`** | Adds/subtracts months from a date. | `F.add_months("date_col", 2)` | `2025-10-08` |
| **`months_between(date1, date2)`** | Returns the number of months between two dates. | `F.months_between(F.current_date(), "date_col")` | `6.25` |
| **`datediff(end, start)`** | Returns the number of days between two dates. | `F.datediff(F.current_date(), "date_col")` | `10` |
| **`last_day(col)`** | Returns the last day of the month. | `F.last_day("date_col")` | `2025-08-31` |
| **`next_day(col, dayOfWeek)`** | Returns the next given day of week after a date. | `F.next_day("date_col", "Sunday")` | `2025-08-10` |
| **`trunc(col, format)`** | Truncates date to the specified unit (`"MM"`, `"YYYY"`). | `F.trunc("date_col", "MM")` | `2025-08-01` |
| **`date_trunc(fmt, col)`** | Truncates timestamp to the given unit (`"hour"`, `"day"`, etc.). | `F.date_trunc("hour", "timestamp_col")` | `2025-08-08 15:00:00` |
| **`from_unixtime(epoch)`** | Converts UNIX timestamp to human-readable time. | `F.from_unixtime(1628391245)` | `2021-08-08 15:34:05` |
| **`unix_timestamp(col, fmt)`** | Converts date/timestamp to UNIX timestamp. | `F.unix_timestamp("timestamp_col", "yyyy-MM-dd HH:mm:ss")` | `1754641245` |
| **`date_format(col, fmt)`** | Formats a date/timestamp as string. | `F.date_format("timestamp_col", "MMM dd, yyyy")` | `Aug 08, 2025` |
| **`from_utc_timestamp(ts, tz)`** | Converts UTC timestamp to given timezone. | `F.from_utc_timestamp("timestamp_col", "PST")` | `2025-08-08 08:30:45` |
| **`to_utc_timestamp(ts, tz)`** | Converts given timezone timestamp to UTC. | `F.to_utc_timestamp("timestamp_col", "PST")` | `2025-08-08 22:30:45` |
| **`current_date()`** | Gets today’s date without time. | `F.current_date()` | `2025-08-08` |
| **`current_timestamp()`** | Gets current date & time. | `F.current_timestamp()` | `2025-08-08 15:45:10` |

---

💡 **Tips:**
- **Date parts extraction**: Use `year()`, `month()`, `dayofmonth()` etc.
- **Date math**: Use `date_add()`, `date_sub()`, `add_months()`.
- **Formatting**: Use `date_format()` for display-friendly strings.
- **Truncation**: Use `trunc()` for dates and `date_trunc()` for timestamps.
- **Time zones**: Use `from_utc_timestamp()` and `to_utc_timestamp()`.

---
