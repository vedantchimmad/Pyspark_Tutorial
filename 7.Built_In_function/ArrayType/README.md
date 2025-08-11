# ArrayType in PySpark

---

## 📌 Overview
In **PySpark**, `ArrayType` is a **data type** from `pyspark.sql.types` used to define **columns containing arrays**.  
It allows you to store multiple values in a single column while maintaining schema support for Spark SQL.

**Import Path**
```python
from pyspark.sql.types import ArrayType, StringType, IntegerType
````

---

## 🛠 Syntax

```python
ArrayType(elementType, containsNull=True)
```

| Parameter      | Type     | Description                                                                    |
| -------------- | -------- | ------------------------------------------------------------------------------ |
| `elementType`  | DataType | The type of elements in the array (e.g., `StringType()`, `IntegerType()` etc.) |
| `containsNull` | Boolean  | Whether the array can contain null values. Default is `True`                   |

---

## 🎯 Example with DataFrame

```python
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, ArrayType, StringType

# Create SparkSession
spark = SparkSession.builder.appName("ArrayTypeExample").getOrCreate()

# Schema with ArrayType
schema = StructType([
    StructField("name", StringType(), True),
    StructField("hobbies", ArrayType(StringType()), True)
])

# Data
data = [
    ("Alice", ["Reading", "Traveling"]),
    ("Bob", ["Swimming", "Gaming"]),
    ("Charlie", ["Hiking", "Photography"])
]

# Create DataFrame
df = spark.createDataFrame(data, schema)
df.show(truncate=False)
```

**Output:**

```
+-------+----------------------+
|name   |hobbies               |
+-------+----------------------+
|Alice  |[Reading, Traveling]  |
|Bob    |[Swimming, Gaming]    |
|Charlie|[Hiking, Photography] |
+-------+----------------------+
```

---

## 🔹 Operations on ArrayType Column

| Function           | Description                              | Example                                                      |
| ------------------ | ---------------------------------------- | ------------------------------------------------------------ |
| `size()`           | Returns the length of the array          | `df.select(size("hobbies")).show()`                          |
| `array_contains()` | Checks if array contains a value         | `df.filter(array_contains("hobbies", "Reading")).show()`     |
| `explode()`        | Creates a new row for each array element | `df.select(explode("hobbies")).show()`                       |
| `concat()`         | Merges multiple array columns            | `df.select(concat("hobbies", array(lit("Cooking")))).show()` |

---

## 🖼 Design Representation

```
+---------+-----------------------------------+
| name    | hobbies                           |
+---------+-----------------------------------+
| Alice   | ["Reading", "Traveling"]          |
| Bob     | ["Swimming", "Gaming"]            |
| Charlie | ["Hiking", "Photography"]         |
+---------+-----------------------------------+

ArrayType: ─────────────────────────────┐
                                         ↓
[ Element1, Element2, Element3, ... ] → Same DataType Elements
```

---

## 🔗 Notes

* `ArrayType` is **nullable by default**, but you can restrict nulls.
* Can be used with **UDFs** for advanced array manipulation.
* Supports SQL-style queries with array functions.

```
SQL Example:
SELECT name, size(hobbies) as hobby_count
FROM people
```
