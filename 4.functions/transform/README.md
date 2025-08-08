# 📌 PySpark `transform()` Function

---

## 🔹 Overview
The **`transform()`** function in PySpark is a **higher-order function** available for both  
**DataFrames** and **RDDs**.  
It allows you to **apply custom transformations** to a DataFrame in a **chainable** and **readable** way.

💡 Think of it like **`pipe()`** in Pandas or function composition —  
you pass a function that takes a DataFrame and returns a modified DataFrame.

---

## 🔹 Syntax
```python
DataFrame.transform(func)
````

| Parameter | Description                                                                       |
| --------- | --------------------------------------------------------------------------------- |
| **func**  | A function that accepts a DataFrame as input and returns a transformed DataFrame. |

**Returns:** New transformed DataFrame.

---

## 🔹 Why Use `transform()`?

* **Improves readability** when applying multiple transformations.
* **Keeps code DRY** (Don't Repeat Yourself) by reusing transformation functions.
* **Chainable** with other DataFrame methods.
* Useful in **function-based pipelines**.

---

## 🔹 Example 1 — Basic Usage

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("TransformExample").getOrCreate()

data = [("Alice", 25), ("Bob", 30), ("Cathy", 28)]
columns = ["Name", "Age"]

df = spark.createDataFrame(data, columns)

# Define a transformation function
def add_age_group(df):
    return df.withColumn("AgeGroup", 
                         (col("Age") / 10).cast("int") * 10)

# Apply using transform
df_transformed = df.transform(add_age_group)

df_transformed.show()
```

**Output**

```
+-----+---+--------+
| Name|Age|AgeGroup|
+-----+---+--------+
|Alice| 25|      20|
|  Bob| 30|      30|
|Cathy| 28|      20|
+-----+---+--------+
```

---

## 🔹 Example 2 — Chaining with Multiple Transforms

```python
from pyspark.sql.functions import upper

def to_uppercase(df):
    return df.withColumn("Name", upper(col("Name")))

def filter_age(df):
    return df.filter(col("Age") > 25)

df_final = (
    df
    .transform(to_uppercase)
    .transform(filter_age)
    .transform(add_age_group)
)

df_final.show()
```

**Output**

```
+----+---+--------+
|Name|Age|AgeGroup|
+----+---+--------+
| BOB| 30|      30|
|CATHY|28|      20|
+----+---+--------+
```

---

## 🔹 Example 3 — Inline Lambda

```python
df_lambda = df.transform(lambda d: d.withColumn("DoubleAge", col("Age") * 2))
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

## 🔹 Key Points

| Feature                | Description                                           |
| ---------------------- | ----------------------------------------------------- |
| **Functional style**   | Pass a function that returns a DataFrame              |
| **Readable pipelines** | Chain multiple transformations                        |
| **Reusable**           | Write once, use everywhere                            |
| **Immutable**          | Returns a new DataFrame without changing the original |

---

✅ **Summary:**
`transform()` in PySpark is great for **clean, reusable, and readable transformation pipelines**.
It doesn't modify the DataFrame in place — it returns a new one that can be chained with more operations.

