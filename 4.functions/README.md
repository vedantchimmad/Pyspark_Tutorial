# 🧩 PySpark Built-in Functions

---
PySpark provides a rich set of **built-in functions** through the `pyspark.sql.functions` module.  
These functions can be used for **data transformations**, **aggregations**, **date/time operations**, **string manipulations**, and more within the DataFrame API.

---

## 📦 Importing Functions

```python
from pyspark.sql.functions import *
````

---

## 🔠 String Functions

| Function                  | Description                         | Example                               |
| ------------------------- | ----------------------------------- | ------------------------------------- |
| `lower(col)`              | Converts string to lowercase        | `df.select(lower("name"))`            |
| `upper(col)`              | Converts string to uppercase        | `df.select(upper("name"))`            |
| `length(col)`             | Returns string length               | `df.select(length("name"))`           |
| `concat(col1, col2)`      | Concatenates columns                | `df.select(concat("fname", "lname"))` |
| `substr(col, start, len)` | Extract substring                   | `df.select(substr("name", 1, 3))`     |
| `trim(col)`               | Removes leading and trailing spaces | `df.select(trim("name"))`             |

---

## 🔢 Numeric Functions

| Function        | Description                 | Example                        |
| --------------- | --------------------------- | ------------------------------ |
| `abs(col)`      | Absolute value              | `df.select(abs("score"))`      |
| `round(col, n)` | Round to `n` decimal places | `df.select(round("value", 2))` |
| `sqrt(col)`     | Square root                 | `df.select(sqrt("value"))`     |
| `ceil(col)`     | Round up                    | `df.select(ceil("value"))`     |
| `floor(col)`    | Round down                  | `df.select(floor("value"))`    |

---

## 📅 Date & Time Functions

| Function               | Description               | Example                               |
| ---------------------- | ------------------------- | ------------------------------------- |
| `current_date()`       | Returns current date      | `df.select(current_date())`           |
| `current_timestamp()`  | Returns current timestamp | `df.select(current_timestamp())`      |
| `datediff(end, start)` | Difference in days        | `df.select(datediff("end", "start"))` |
| `date_add(date, days)` | Add days to date          | `df.select(date_add("start", 7))`     |
| `year(col)`            | Extract year              | `df.select(year("dob"))`              |
| `month(col)`           | Extract month             | `df.select(month("dob"))`             |

---

## 🧮 Aggregate Functions

| Function     | Description           | Example                    |
| ------------ | --------------------- | -------------------------- |
| `count(col)` | Count non-null values | `df.select(count("id"))`   |
| `sum(col)`   | Sum of column values  | `df.select(sum("salary"))` |
| `avg(col)`   | Average value         | `df.select(avg("score"))`  |
| `min(col)`   | Minimum value         | `df.select(min("age"))`    |
| `max(col)`   | Maximum value         | `df.select(max("salary"))` |

---

## 🧠 Conditional Functions

| Function                 | Description           | Example                                                      |
| ------------------------ | --------------------- | ------------------------------------------------------------ |
| `when(condition, value)` | If-then-else logic    | `df.select(when(df.age > 30, "Senior").otherwise("Junior"))` |
| `isnull(col)`            | Check for null values | `df.filter(isnull("name"))`                                  |
| `coalesce(col1, col2)`   | First non-null value  | `df.select(coalesce("col1", "col2"))`                        |

---

## 🔗 Array & Map Functions

| Function                | Description                        | Example                         |
| ----------------------- | ---------------------------------- | ------------------------------- |
| `split(col, delimiter)` | Splits string into array           | `df.select(split("name", " "))` |
| `size(col)`             | Size of array or map               | `df.select(size("tags"))`       |
| `explode(col)`          | Returns a new row for each element | `df.select(explode("items"))`   |

---

## 🏷️ Miscellaneous Functions

| Function                        | Description                          | Example                                              |
| ------------------------------- | ------------------------------------ | ---------------------------------------------------- |
| `lit(value)`                    | Create a column with a literal value | `df.select(lit("static_value"))`                     |
| `monotonically_increasing_id()` | Unique ID                            | `df.withColumn("id", monotonically_increasing_id())` |
| `rand()`                        | Generate random number               | `df.select(rand())`                                  |

---

## 🔄 Example: Using Multiple Functions

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, when, avg

spark = SparkSession.builder.appName("FuncExample").getOrCreate()

data = [("Alice", 34), ("Bob", 25), ("Charlie", 45)]
df = spark.createDataFrame(data, ["name", "age"])

df_transformed = df.withColumn("NAME_UPPER", upper(col("name"))) \
                   .withColumn("CATEGORY", when(col("age") > 30, "Senior").otherwise("Junior"))

df_transformed.show()
```

---

## 🧠 Tip:

To explore all functions:

```python
import pyspark.sql.functions as F
dir(F)
```
