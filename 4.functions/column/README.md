
# 🧮 PySpark Column Functions

PySpark provides a rich set of **column functions** in `pyspark.sql.functions` module  
to perform transformations and computations on DataFrame columns.

---

## 🔖 Import Statement

```python
from pyspark.sql.functions import *
````

---

## 🗂️ Categories of Column Functions

| Category             | Function Examples                                                                      |
| -------------------- | -------------------------------------------------------------------------------------- |
| **Math**             | `abs()`, `sqrt()`, `round()`, `exp()`, `log()`, `pow()`, `sin()`, `cos()`, `tan()`     |
| **String**           | `concat()`, `substr()`, `length()`, `lower()`, `upper()`, `trim()`, `regexp_replace()` |
| **Date/Time**        | `current_date()`, `current_timestamp()`, `datediff()`, `add_months()`, `year()`        |
| **Aggregation**      | `count()`, `sum()`, `avg()`, `min()`, `max()`, `mean()`                                |
| **Conditional**      | `when()`, `otherwise()`, `isnull()`, `coalesce()`, `lit()`                             |
| **Window Functions** | `row_number()`, `rank()`, `dense_rank()`, `lead()`, `lag()`                            |
| **Collection**       | `array()`, `explode()`, `size()`, `map()`                                              |
| **Null Handling**    | `isnull()`, `isnotnull()`, `fillna()`, `dropna()`                                      |
| **JSON/Struct/Map**  | `get_json_object()`, `from_json()`, `to_json()`, `col()`, `struct()`                   |
| **Misc**             | `col()`, `alias()`, `lit()`, `expr()`, `monotonically_increasing_id()`                 |

---

## 🔍 Column Functions with Example Code

| Function                        | Description         | Example Code                                         |
| ------------------------------- | ------------------- | ---------------------------------------------------- |
| `col("col")`                    | Refers to column    | `df.select(col("age"))`                              |
| `lit(1)`                        | Add literal value   | `df.withColumn("flag", lit(1))`                      |
| `when(cond, val)`               | If-then logic       | `df.withColumn("type", when(df.age > 30, "Senior"))` |
| `concat()`                      | Concatenate strings | `df.select(concat(col("fname"), col("lname")))`      |
| `length(col)`                   | Length of string    | `df.select(length("name"))`                          |
| `lower()`, `upper()`            | Case conversion     | `df.select(lower("name"), upper("name"))`            |
| `substr(col, start, len)`       | Substring           | `df.select(substr("name", 1, 3))`                    |
| `round(col, scale)`             | Round float         | `df.select(round("salary", 2))`                      |
| `current_date()`                | Today's date        | `df.withColumn("today", current_date())`             |
| `datediff()`                    | Difference in days  | `df.select(datediff(current_date(), col("dob")))`    |
| `year(col)`                     | Extract year        | `df.select(year("dob"))`                             |
| `array()`                       | Create array column | `df.select(array("col1", "col2"))`                   |
| `explode()`                     | Explode array       | `df.select(explode("hobbies"))`                      |
| `count()`                       | Count rows          | `df.select(count("*"))`                              |
| `sum()`, `avg()`                | Sum, average        | `df.select(sum("salary"), avg("salary"))`            |
| `rank()`                        | Rank over window    | `df.withColumn("rank", rank().over(windowSpec))`     |
| `monotonically_increasing_id()` | Add unique ID       | `df.withColumn("id", monotonically_increasing_id())` |
| `regexp_replace()`              | Replace using regex | `df.select(regexp_replace("name", "a", "@"))`        |
| `get_json_object()`             | Extract from JSON   | `df.select(get_json_object("json_col", "$.field"))`  |

---

## 🧠 Best Practice Tip

Use built-in functions from `pyspark.sql.functions` **instead of UDFs** for:

* Better performance (they're optimized)
* Catalyst optimization
* Portability to other languages (Scala/Java)


---
# 🧪 PySpark Column Functions – With DataFrame Examples

This section demonstrates various commonly used **PySpark column functions** using a sample DataFrame.

---

### 🧱 Create Sample DataFrame

```python
data = [
    ("James", "Bond", "100", None),
    ("Ann", "Varsa", "200", 'F'),
    ("Tom Cruise", "XXX", "400", ''),
    ("Tom Brand", None, "400", 'M')
]
columns = ["fname", "lname", "id", "gender"]
df = spark.createDataFrame(data, columns)
````

---

### 🔧 Column Function Examples

#### 1. `alias()` – Rename a column

```python
from pyspark.sql.functions import expr

df.select(
    df.fname.alias("first_name"),
    df.lname.alias("last_name")
).show()
```

---

#### 2. `asc()` and `desc()` – Sort order

```python
df.sort(df.fname.asc()).show()
df.sort(df.fname.desc()).show()
```

---

#### 3. `cast()` – Convert data type

```python
df.select(df.fname, df.id.cast("int")).printSchema()
```

---

#### 4. `between()` – Check if values are in range

```python
df.filter(df.id.between(100, 300)).show()
```

---

#### 5. `contains()` – Check if column contains a substring

```python
df.filter(df.fname.contains("Cruise")).show()
```

---

#### 6. `startswith()` and `endswith()` – Substring match

```python
df.filter(df.fname.startswith("T")).show()
df.filter(df.fname.endswith("Cruise")).show()
```

---

#### 7. `isNull()` and `isNotNull()` – Check for nulls

```python
df.filter(df.lname.isNull()).show()
df.filter(df.lname.isNotNull()).show()
```

---

#### 8. `like()` – SQL LIKE pattern matching

```python
df.select("fname", "lname", "id") \
  .filter(df.fname.like("%om")).show()
```

---

#### 9. `substr()` – Substring from column

```python
df.select(df.fname.substr(1, 2).alias("substr")).show()
```

---

#### 10. `when()` and `otherwise()` – Conditional logic

```python
from pyspark.sql.functions import when

df.select(
    df.fname, df.lname,
    when(df.gender == "M", "Male")
    .when(df.gender == "F", "Female")
    .when(df.gender == None, "")
    .otherwise(df.gender)
    .alias("new_gender")
).show()
```

---

#### 11. `isin()` – Check if column value exists in list

```python
li = ["100", "200"]
df.select("fname", "lname", "id") \
  .filter(df.id.isin(li)).show()
```

---
## 🧭 Different Ways to Access Columns in PySpark

PySpark provides multiple ways to **access columns** in a DataFrame. These are essential for selection, transformation, and filtering operations.

---

### 🧱 Sample DataFrame

```python
data = [("John", 25), ("Alice", 30)]
columns = ["name", "age"]
df = spark.createDataFrame(data, columns)
````

---

### ✅ 1. Dot Notation (`df.colName`)

```python
df.select(df.name).show()
```

> ⚠️ Use only if column names are simple (no spaces, special characters)

---

### ✅ 2. Bracket Notation (`df["colName"]`)

```python
df.select(df["age"]).show()
```

> ✅ Safe for all column names, including ones with spaces or reserved characters.

---

### ✅ 3. `col()` Function (Recommended for expressions)

```python
from pyspark.sql.functions import col

df.select(col("name")).show()
```

> 🔧 Useful when writing expressions, filters, etc.

---

### ✅ 4. `df.selectExpr("colExpr")` – SQL-like Expression

```python
df.selectExpr("age * 2 as double_age").show()
```

> 🧠 Allows SQL expressions directly.

---

### ✅ 5. Using `expr()` for column expression

```python
from pyspark.sql.functions import expr

df.select(expr("age + 10").alias("age_plus_10")).show()
```

---

### 📊 Comparison Table

| Method            | Syntax                   | Notes                                      |
| ----------------- | ------------------------ | ------------------------------------------ |
| Dot notation      | `df.col`                 | Simple, fails on spaces/special characters |
| Bracket notation  | `df["col"]`              | Safe for all column names                  |
| `col()` function  | `col("col")`             | Best for transformations                   |
| `selectExpr()`    | `selectExpr("expr")`     | SQL-style, supports aliasing               |
| `expr()`          | `expr("expr")`           | SQL expressions in transformations         |
| Row object access | `row["col"]` or `row[i]` | After using `collect()` or `first()`       |

---

📝 **Best Practice**: Use `col()` for code clarity and flexibility in complex transformations.





