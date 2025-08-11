# JSON in PySpark  

---
PySpark provides built-in functions to read, write, and process JSON data efficiently.  
JSON (JavaScript Object Notation) is a lightweight format used for storing and transporting data, especially in distributed applications.  

---

## 1. **Reading JSON Data**

PySpark can directly read JSON files into a DataFrame.

```python
# Read JSON file
df = spark.read.json("data.json")

# Show DataFrame
df.show(truncate=False)
df.printSchema()
````

| Parameter   | Description                                                                    |
| ----------- | ------------------------------------------------------------------------------ |
| `path`      | Path to the JSON file(s). Supports wildcards like `*.json`.                    |
| `.option()` | Used to configure parameters such as schema inference, multiline reading, etc. |
| `.schema()` | Define a custom schema instead of inferring.                                   |

**Example with options:**

```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

df = spark.read.option("multiline", True) \
               .schema(schema) \
               .json("data.json")

df.show()
```

---

## 2. **Writing JSON Data**

```python
df.write.json("output_folder")
```

| Method        | Description                                          |
| ------------- | ---------------------------------------------------- |
| `.json(path)` | Writes DataFrame to JSON format.                     |
| `.mode()`     | Save mode: `overwrite`, `append`, `ignore`, `error`. |

**Example:**

```python
df.write.mode("overwrite").json("output_json")
```

---

## 3. **Working with JSON Columns**

Sometimes JSON data is stored as a string in a DataFrame column.
PySpark provides functions to parse, query, and generate JSON strings.

| Function            | Description                                                                | Example                                                         |
| ------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------- |
| `from_json()`       | Converts JSON string column into a structured format (StructType/MapType). | `df.withColumn("parsed", from_json("json_col", schema))`        |
| `to_json()`         | Converts a struct/map column to JSON string.                               | `df.withColumn("json_str", to_json("struct_col"))`              |
| `get_json_object()` | Extracts a specific JSON field as string using JSON path.                  | `df.select(get_json_object("json_col", "$.name"))`              |
| `schema_of_json()`  | Infers schema from a JSON string.                                          | `spark.range(1).select(schema_of_json(lit('{"name":"John"}')))` |

**Example:**

```python
from pyspark.sql.functions import from_json, to_json, get_json_object, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Sample data
data = [('{"name":"James","age":30}',)]
df = spark.createDataFrame(data, ["json_str"])

# Define schema
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

# Parse JSON
df_parsed = df.withColumn("parsed", from_json(col("json_str"), schema))
df_parsed.show(truncate=False)

# Extract a field
df_parsed.select(get_json_object(col("json_str"), "$.name").alias("name_only")).show()
```

---

## 4. **Example of Reading, Transforming, and Writing JSON**

```python
from pyspark.sql.functions import col

# Read JSON
df = spark.read.json("people.json")

# Select required fields
df_selected = df.select(col("name"), col("age"))

# Write to JSON
df_selected.write.mode("overwrite").json("output_people")
```

---

✅ **Key Notes**

* Supports reading multiple JSON files at once (wildcards).
* Can handle multiline JSON using `.option("multiline", True)`.
* JSON columns can be parsed into complex nested structures.
* Writing JSON results in one file per partition unless `.coalesce()` or `.repartition(1)` is used.

