# 📅 `months_between` in PySpark

---

## 📝 Overview
The `months_between` function in PySpark returns the **number of months** between two dates.  
It can return fractional months depending on the difference in days between the two dates.

**Import Path**
```python
from pyspark.sql.functions import months_between
````

---

## 🛠 Syntax

```python
months_between(endDate, startDate, roundOff=True)
```

| Parameter   | Description                                                                     |
| ----------- | ------------------------------------------------------------------------------- |
| `endDate`   | **Required**. Column or date string representing the later date.                |
| `startDate` | **Required**. Column or date string representing the earlier date.              |
| `roundOff`  | **Optional**. Boolean flag to round off to 8 decimal places. Default is `True`. |

**Return Type:**
`DoubleType` (number of months as a float).

---

## 🎯 Example 1: Basic Usage

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import months_between, to_date

spark = SparkSession.builder.appName("MonthsBetweenExample").getOrCreate()

data = [("2025-08-11", "2025-01-11"), ("2025-08-11", "2024-08-11")]
df = spark.createDataFrame(data, ["end_date", "start_date"])

df = df.withColumn(
    "months_diff",
    months_between(to_date("end_date"), to_date("start_date"))
)

df.show()
```

**Output:**

```
+----------+----------+-----------+
| end_date |start_date|months_diff|
+----------+----------+-----------+
|2025-08-11|2025-01-11|        7.0|
|2025-08-11|2024-08-11|       12.0|
+----------+----------+-----------+
```

---

## 🎯 Example 2: Fractional Months

```python
data = [("2025-08-15", "2025-08-01")]
df = spark.createDataFrame(data, ["end_date", "start_date"])

df = df.withColumn(
    "months_diff_fraction",
    months_between(to_date("end_date"), to_date("start_date"))
)

df.show()
```

**Output:**

```
+----------+----------+-------------------+
| end_date |start_date|months_diff_fraction|
+----------+----------+-------------------+
|2025-08-15|2025-08-01| 0.45161290322580644|
+----------+----------+-------------------+
```

---

## 🎯 Example 3: Reverse Order (Negative Result)

```python
data = [("2025-01-11", "2025-08-11")]
df = spark.createDataFrame(data, ["end_date", "start_date"])

df = df.withColumn(
    "months_diff",
    months_between(to_date("end_date"), to_date("start_date"))
)

df.show()
```

**Output:**

```
+----------+----------+-----------+
| end_date |start_date|months_diff|
+----------+----------+-----------+
|2025-01-11|2025-08-11|      -7.0 |
+----------+----------+-----------+
```

---

## 🔍 Key Points

* If `endDate` is earlier than `startDate`, result will be **negative**.
* Takes into account leap years and varying month lengths.
* Returns a **fraction** if the dates are not exactly the same day of the month.
* Works with both **string dates** and **date columns**.

---

