# 🗺️ PySpark `MapType`

---
In PySpark, `MapType` is a **data type** used in **schemas** to represent a map (dictionary)  
where each key is associated with a value.  
It is similar to Python's `dict` but is a **distributed column type** in Spark DataFrames.

---

## 🛠 Syntax

```python
from pyspark.sql.types import MapType, StringType, IntegerType

MapType(keyType, valueType, valueContainsNull=True)
````

| Parameter           | Description                                                      |
| ------------------- | ---------------------------------------------------------------- |
| `keyType`           | Data type of keys (e.g., `StringType()`).                        |
| `valueType`         | Data type of values (e.g., `IntegerType()`).                     |
| `valueContainsNull` | Boolean, whether the value can contain nulls. Default is `True`. |

---

## ⚡ Key Points

* Keys **cannot** be `null`.
* Values can be `null` depending on `valueContainsNull`.
* Useful for storing **JSON-like structures** in a column.
* Often used when parsing nested data formats (JSON, Avro, etc.).

---

## 📌 Example 1: Creating a DataFrame with `MapType`

```python
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, MapType, StringType, IntegerType

spark = SparkSession.builder.appName("MapTypeExample").getOrCreate()

schema = StructType([
    StructField("id", StringType(), True),
    StructField("properties", MapType(StringType(), IntegerType()), True)
])

data = [
    ("1", {"math": 85, "science": 90}),
    ("2", {"math": 78, "science": 88}),
    ("3", {"math": 92, "science": None})
]

df = spark.createDataFrame(data, schema)
df.show(truncate=False)
```

**Output**

```
+---+----------------------+
|id |properties            |
+---+----------------------+
|1  |{math -> 85, science -> 90}|
|2  |{math -> 78, science -> 88}|
|3  |{math -> 92, science -> null}|
+---+----------------------+
```

---

## 📌 Example 2: Accessing Map Values

```python
from pyspark.sql import functions as F

# Access a single key from the map
df.select(
    "id",
    F.col("properties")["math"].alias("math_score")
).show()

# Access multiple keys (using getItem)
df.select(
    "id",
    F.col("properties").getItem("science").alias("science_score")
).show()
```

---

## 📌 Example 3: Filtering Based on Map Values

```python
df.filter(F.col("properties")["math"] > 80).show()
```

---

## 📌 Example 4: Creating Map Column from Two Arrays

```python
df2 = spark.createDataFrame(
    [(1, ["math", "science"], [85, 90])],
    ["id", "subjects", "scores"]
)

df2.withColumn("properties", F.map_from_arrays(F.col("subjects"), F.col("scores"))).show(truncate=False)
```

---

## 🚀 When to Use

* Handling semi-structured data like JSON.
* Storing dynamic key-value attributes per row.
* Working with configuration-like or metadata information in DataFrames.

---

## 🛑 Common Mistakes

* Expecting keys to allow nulls (not supported).
* Forgetting to define `MapType` in the schema when reading complex data.

---

