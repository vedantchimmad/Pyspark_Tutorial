# 📌 PySpark — User Defined Functions (UDF)

---

## 🔹 Overview
A **User Defined Function (UDF)** in PySpark allows you to **write custom functions** in Python  
and apply them to **DataFrame columns** just like built-in Spark SQL functions.

💡 Useful when Spark’s built-in functions do not meet your requirements.

---

## 🔹 Syntax
```python
from pyspark.sql.functions import udf
from pyspark.sql.types import DataType

udf_name = udf(lambda_function_or_python_function, returnType=DataType)
````

| Parameter                                  | Description                                                                        |
| ------------------------------------------ | ---------------------------------------------------------------------------------- |
| **lambda\_function\_or\_python\_function** | Python function to apply.                                                          |
| **returnType**                             | Data type of the return value (from `pyspark.sql.types`). Required for DataFrames. |

---

## 🔹 Steps to Use a UDF

1. **Write a Python function** (normal or lambda).
2. **Register it as a UDF** with the return type.
3. **Use it in DataFrame transformations** with `withColumn()` or `select()`.

---

## 🔹 Example 1 — Basic UDF

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName("UDFExample").getOrCreate()

data = [("Alice", 25), ("Bob", 30), ("Cathy", 28)]
columns = ["Name", "Age"]

df = spark.createDataFrame(data, columns)

# Step 1: Define Python function
def age_category(age):
    if age < 26:
        return "Young"
    elif age < 30:
        return "Adult"
    else:
        return "Senior"

# Step 2: Register UDF
age_category_udf = udf(age_category, StringType())

# Step 3: Apply to DataFrame
df_new = df.withColumn("Category", age_category_udf(df["Age"]))
df_new.show()
```

**Output**

```
+-----+---+--------+
| Name|Age|Category|
+-----+---+--------+
|Alice| 25|   Young|
|  Bob| 30|  Senior|
|Cathy| 28|   Adult|
+-----+---+--------+
```

---

## 🔹 Example 2 — Using Lambda with UDF

```python
from pyspark.sql.types import IntegerType

double_udf = udf(lambda x: x * 2, IntegerType())
df_lambda = df.withColumn("DoubleAge", double_udf(df["Age"]))
df_lambda.show()
```

**Output**

```
+-----+---+---------+
| Name|Age|DoubleAge|
+-----+---+---------+
|Alice| 25|       50|
|  Bob| 30|       60|
|Cathy| 28|       56|
+-----+---+---------+
```

---

## 🔹 Example 3 — Register UDF for SQL Queries

```python
# Register as SQL function
spark.udf.register("age_category_sql", age_category, StringType())

df.createOrReplaceTempView("people")

spark.sql("""
SELECT Name, Age, age_category_sql(Age) AS Category
FROM people
""").show()
```

**Output**

```
+-----+---+--------+
| Name|Age|Category|
+-----+---+--------+
|Alice| 25|   Young|
|  Bob| 30|  Senior|
|Cathy| 28|   Adult|
+-----+---+--------+
```

---

## 🔹 Performance Note ⚡

* UDFs can be **slower** than Spark’s built-in functions because:

    * They run in **Python** (not optimized JVM code).
    * Serialization/deserialization overhead.
* Always check if a **built-in PySpark function** exists before writing a UDF.

---

## 🔹 Key Points

| Feature            | Description                          |
| ------------------ | ------------------------------------ |
| **Custom logic**   | Write Python code for transformation |
| **Type safe**      | Must define output data type         |
| **SQL compatible** | Can register for SQL use             |
| **Performance**    | Slower than native Spark functions   |

---

✅ **Summary:**
UDFs in PySpark let you extend Spark's functionality with your **own Python functions**,
but use them wisely to avoid performance hits.

