# 📌 PySpark `show()` Function

---

## 🔹 Overview
The **`show()`** function in PySpark is used to **display DataFrame contents** in a tabular format.  
It’s mainly used for **debugging** or **quick inspection** of the data.

---

## 🔹 Syntax
```python
DataFrame.show(n=20, truncate=True, vertical=False)
````

| Parameter    | Description                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **n**        | Number of rows to display (default = 20).                                                                                                         |
| **truncate** | If `True` (default), truncates strings longer than 20 characters. If an integer, truncates to that length. If `False`, shows full column content. |
| **vertical** | If `True`, displays rows vertically (good for many columns).                                                                                      |

---

## 🔹 Example 1 — Basic Usage

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ShowExample").getOrCreate()

data = [
    ("Alice", 25, "HR"),
    ("Bob", 30, "IT"),
    ("Cathy", 28, "Finance")
]
columns = ["Name", "Age", "Dept"]

df = spark.createDataFrame(data, columns)

# Show first 20 rows (default)
df.show()
```

**Output**

```
+-----+---+-------+
| Name|Age|   Dept|
+-----+---+-------+
|Alice| 25|     HR|
|  Bob| 30|     IT|
|Cathy| 28|Finance|
+-----+---+-------+
```

---

## 🔹 Example 2 — Display Specific Number of Rows

```python
df.show(2)
```

**Output**

```
+-----+---+----+
| Name|Age|Dept|
+-----+---+----+
|Alice| 25|  HR|
|  Bob| 30|  IT|
+-----+---+----+
```

---

## 🔹 Example 3 — Show Without Truncating

```python
df_long = spark.createDataFrame(
    [("Alice", "This is a very long department name exceeding default length")],
    ["Name", "Dept"]
)

df_long.show(truncate=False)
```

**Output**

```
+-----+--------------------------------------------------------------+
|Name |Dept                                                          |
+-----+--------------------------------------------------------------+
|Alice|This is a very long department name exceeding default length  |
+-----+--------------------------------------------------------------+
```

---

## 🔹 Example 4 — Vertical Display

```python
df.show(vertical=True)
```

**Output**

```
-RECORD 0-----
 Name | Alice
 Age  | 25
 Dept | HR
-RECORD 1-----
 Name | Bob
 Age  | 30
 Dept | IT
...
```

---

## 🔹 Key Points

| Feature              | Description                           |
| -------------------- | ------------------------------------- |
| **Quick data check** | Ideal for debugging                   |
| **Custom row count** | Pass `n` to see more/less rows        |
| **Full text**        | Use `truncate=False`                  |
| **Vertical view**    | Use `vertical=True` for wide datasets |

---

✅ **Summary:**

* **`show()`** is non-returning (prints to console).
* Best for **quick inspection** — not for saving or further processing.
* Use `truncate=False` for full visibility of long strings.
