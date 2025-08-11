# PySpark Window Functions

---

## 🪟 What are Window Functions?

In **PySpark**, window functions allow you to perform calculations across a set of rows that are related to the current row, without collapsing them into a single output like aggregation functions do.  
They are defined using a **`Window` specification**, which determines **partitioning**, **ordering**, and the range of rows involved in the calculation.

---

## 🛠 Components of a Window Specification

1. **Partitioning**  
   - Groups rows into partitions (like SQL `GROUP BY`), but keeps them available for row-by-row calculations.
   - Defined using `.partitionBy()`.

2. **Ordering**  
   - Defines the order of rows within each partition.
   - Defined using `.orderBy()`.

3. **Frame Specification** *(Optional)*  
   - Defines a range of rows relative to the current row for computation.  
   - Examples:
     - `rowsBetween(start, end)`
     - `rangeBetween(start, end)`

---

## 📦 Commonly Used Window Functions

| Function | Description | Example |
|----------|-------------|---------|
| `row_number()` | Assigns a unique sequential number to rows within a partition. | `row_number().over(windowSpec)` |
| `rank()` | Gives ranking with gaps in case of ties. | `rank().over(windowSpec)` |
| `dense_rank()` | Gives ranking without gaps in case of ties. | `dense_rank().over(windowSpec)` |
| `ntile(n)` | Divides rows into `n` buckets and assigns a bucket number. | `ntile(4).over(windowSpec)` |
| `lead()` | Returns the value from the next row within the partition. | `lead("col", 1).over(windowSpec)` |
| `lag()` | Returns the value from the previous row within the partition. | `lag("col", 1).over(windowSpec)` |
| `sum()` | Running or cumulative sum over a window frame. | `sum("col").over(windowSpec)` |
| `avg()` | Running average over a window frame. | `avg("col").over(windowSpec)` |
| `min()` | Minimum value over a window frame. | `min("col").over(windowSpec)` |
| `max()` | Maximum value over a window frame. | `max("col").over(windowSpec)` |

---

## 💻 Example

```python
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, rank, dense_rank, lead, lag, sum, avg

# Create Spark session
spark = SparkSession.builder.appName("WindowFunctionExample").getOrCreate()

# Sample Data
data = [
    ("James", "Sales", 3000),
    ("Michael", "Sales", 4600),
    ("Robert", "Sales", 4100),
    ("Maria", "Finance", 3000),
    ("James", "Finance", 3000),
    ("Scott", "Finance", 3300),
    ("Jen", "Finance", 3900),
    ("Jeff", "Marketing", 3000),
    ("Kumar", "Marketing", 2000)
]
columns = ["employee_name", "department", "salary"]

df = spark.createDataFrame(data, columns)

# Define Window Specification
windowSpec = Window.partitionBy("department").orderBy("salary")

# Apply Window Functions
df.select(
    "employee_name",
    "department",
    "salary",
    row_number().over(windowSpec).alias("row_number"),
    rank().over(windowSpec).alias("rank"),
    dense_rank().over(windowSpec).alias("dense_rank"),
    lead("salary", 1).over(windowSpec).alias("next_salary"),
    lag("salary", 1).over(windowSpec).alias("prev_salary"),
    sum("salary").over(windowSpec).alias("running_total"),
    avg("salary").over(windowSpec).alias("running_avg")
).show()
````

---

## 📊 Output Example

| employee\_name | department | salary | row\_number | rank | dense\_rank | next\_salary | prev\_salary | running\_total | running\_avg |
| -------------- | ---------- | ------ | ----------- | ---- | ----------- | ------------ | ------------ | -------------- | ------------ |
| Kumar          | Marketing  | 2000   | 1           | 1    | 1           | 3000         | NULL         | 2000           | 2000.0       |
| Jeff           | Marketing  | 3000   | 2           | 2    | 2           | NULL         | 2000         | 5000           | 2500.0       |
| Maria          | Finance    | 3000   | 1           | 1    | 1           | 3000         | NULL         | 3000           | 3000.0       |
| James          | Finance    | 3000   | 2           | 1    | 1           | 3300         | 3000         | 6000           | 3000.0       |
| Scott          | Finance    | 3300   | 3           | 3    | 2           | 3900         | 3000         | 9300           | 3100.0       |
| Jen            | Finance    | 3900   | 4           | 4    | 3           | NULL         | 3300         | 13200          | 3300.0       |
| James          | Sales      | 3000   | 1           | 1    | 1           | 4100         | NULL         | 3000           | 3000.0       |
| Robert         | Sales      | 4100   | 2           | 2    | 2           | 4600         | 3000         | 7100           | 3550.0       |
| Michael        | Sales      | 4600   | 3           | 3    | 3           | NULL         | 4100         | 11700          | 3900.0       |

---

## 🎯 Key Notes

* Window functions **do not** reduce rows like `groupBy()`; they keep all rows intact.
* Can be used for **ranking**, **running totals**, **moving averages**, and **time-based calculations**.
* Useful in **analytics and reporting** without losing row-level detail.


