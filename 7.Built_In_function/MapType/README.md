# 🗺️ `MapType` in PySpark

---

## 📝 Overview
`MapType` is a **data type** in PySpark used to represent **key-value pairs** in a DataFrame column.  
It is part of the `pyspark.sql.types` module and is useful when you need to store **dictionary-like structures** inside a single column.

**Import Path**
```python
from pyspark.sql.types import MapType, StringType, IntegerType
````

---

## 🛠 Syntax

```python
MapType(keyType, valueType, valueContainsNull=True)
```

| Parameter           | Description                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------------------- |
| `keyType`           | **Required**. Data type of keys (e.g., `StringType()`).                                         |
| `valueType`         | **Required**. Data type of values (e.g., `IntegerType()`).                                      |
| `valueContainsNull` | **Optional**. Boolean flag indicating whether map values can contain `null`. Default is `True`. |

**Return Type:**
`MapType` object (used inside a DataFrame schema).

---

## 🎯 Example 1: Creating a DataFrame with `MapType`

```python
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, MapType, StringType, IntegerType

spark = SparkSession.builder.appName("MapTypeExample").getOrCreate()

schema = StructType([
    StructField("name", StringType(), True),
    StructField("properties", MapType(StringType(), StringType()), True)
])

data = [
    ("Alice", {"hair": "brown", "eye": "blue"}),
    ("Bob", {"hair": "black", "eye": "green"})
]

df = spark.createDataFrame(data, schema)
df.show(truncate=False)
```

**Output:**

```
+-----+------------------------------+
|name |properties                    |
+-----+------------------------------+
|Alice|{hair -> brown, eye -> blue}   |
|Bob  |{hair -> black, eye -> green}  |
+-----+------------------------------+
```

---

## 🎯 Example 2: Accessing Map Values

```python
from pyspark.sql import functions as F

df.select(
    "name",
    F.col("properties").getItem("hair").alias("hair_color")
).show()
```

**Output:**

```
+-----+----------+
|name |hair_color|
+-----+----------+
|Alice|brown     |
|Bob  |black     |
+-----+----------+
```

---

## 🎯 Example 3: Creating a Map Column Dynamically

```python
df2 = df.withColumn(
    "skills_map",
    F.create_map(F.lit("Python"), F.lit(5), F.lit("Java"), F.lit(4))
)

df2.show(truncate=False)
```

**Output:**

```
+-----+------------------------------+-------------------------+
|name |properties                    |skills_map               |
+-----+------------------------------+-------------------------+
|Alice|{hair -> brown, eye -> blue}   |{Python -> 5, Java -> 4} |
|Bob  |{hair -> black, eye -> green}  |{Python -> 5, Java -> 4} |
+-----+------------------------------+-------------------------+
```

---

## 🖼 Visual Representation

| **Name** | **Properties (Map)**      |
| -------- | ------------------------- |
| Alice    | hair → brown, eye → blue  |
| Bob      | hair → black, eye → green |

---

## 🔍 Key Points

* **Keys must be unique** in a `MapType`.
* Can **nest** `MapType` inside other complex types like `ArrayType` or `StructType`.
* Useful for **flexible key-value storage** without defining fixed column names.
* Works seamlessly with **Spark SQL functions** like `getItem`, `map_keys`, `map_values`, `create_map`.

---
