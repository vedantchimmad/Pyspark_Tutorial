# 🔗 `concat_ws` in PySpark

---

## 📝 Overview
`concat_ws` stands for **Concatenate With Separator**.  
It concatenates multiple string columns or arrays into a **single string**, inserting a **specified separator** between each value.

**Import Path**
```python
from pyspark.sql import functions as F
````

---

## 🛠 Syntax

```python
concat_ws(sep, *cols)
```

| Parameter | Description                                                                                 |
| --------- | ------------------------------------------------------------------------------------------- |
| `sep`     | **Required**. The separator to use between concatenated values (e.g., `","`, `"-"`, `" "`). |
| `*cols`   | **Required**. One or more string columns or array columns to concatenate.                   |

---

## 🎯 Example 1: Concatenate String Columns

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Create SparkSession
spark = SparkSession.builder.appName("ConcatWSExample").getOrCreate()

# Sample Data
data = [
    ("John", "Doe", "New York"),
    ("Jane", "Smith", "London"),
    ("Mike", None, "Sydney")
]

# Create DataFrame
df = spark.createDataFrame(data, ["first_name", "last_name", "city"])

# Using concat_ws
result = df.withColumn(
    "full_info",
    F.concat_ws(", ", "first_name", "last_name", "city")
)

result.show(truncate=False)
```

**Output:**

```
+----------+---------+--------+-------------------+
|first_name|last_name|city    |full_info          |
+----------+---------+--------+-------------------+
|John      |Doe      |New York|John, Doe, New York|
|Jane      |Smith    |London  |Jane, Smith, London|
|Mike      |null     |Sydney  |Mike, Sydney       |
+----------+---------+--------+-------------------+
```

💡 `null` values are **ignored** automatically.

---

## 🎯 Example 2: Concatenate Array Elements

```python
data2 = [
    (["apple", "banana", "cherry"],),
    (["cat", "dog"],)
]

df2 = spark.createDataFrame(data2, ["fruits"])

result2 = df2.withColumn(
    "fruits_string",
    F.concat_ws(" | ", "fruits")
)

result2.show(truncate=False)
```

**Output:**

```
+----------------------+----------------+
|fruits                |fruits_string   |
+----------------------+----------------+
|[apple, banana, cherry]|apple | banana | cherry|
|[cat, dog]             |cat | dog      |
+----------------------+----------------+
```

---

## 🔍 Key Points

* Ignores `null` values without adding extra separators.
* Works with **string columns** and **array columns**.
* The separator can be any string (space, comma, dash, etc.).

---

## 🖼 Visual Representation

```
[first_name]  [last_name]  [city]
    John         Doe       New York
      ↓ concat_ws(", ")
"John, Doe, New York"
```

