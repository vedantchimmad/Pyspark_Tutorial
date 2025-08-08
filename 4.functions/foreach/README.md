# 🔄 PySpark `foreach()` Function

---
The `foreach()` function in PySpark is used to apply a function to **each element** in an RDD or DataFrame **without returning a new dataset**.  
It’s mainly used for **side effects** such as writing to a database, logging, or performing external API calls.

---

## 🛠 Syntax

```python
RDD.foreach(f)
````

| Parameter | Description                                                                   |
| --------- | ----------------------------------------------------------------------------- |
| `f`       | Function to apply to each element of the RDD/DataFrame. No value is returned. |

---

## ⚠️ Important Notes

* Works **on each partition node** (function runs on executors, not the driver).
* Does **not** return anything.
* Should only be used for **actions** with side effects (writing to external systems).
* For transformations, use `map()` or `mapPartitions()` instead.

---

## 📌 Example 1: Using `foreach()` on an RDD

```python
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])

def print_element(x):
    print(f"Element: {x}")

rdd.foreach(print_element)
```

> Note: Printing inside `foreach()` happens on the **executors**, so it may not appear in the driver console.

---

## 📌 Example 2: Writing Data to an External File

```python
def save_to_file(row):
    with open("/tmp/output.txt", "a") as f:
        f.write(str(row) + "\n")

rdd = spark.sparkContext.parallelize(["apple", "banana", "cherry"])
rdd.foreach(save_to_file)
```

---

## 📌 Example 3: `foreach()` on DataFrame Rows

```python
from pyspark.sql import Row

df = spark.createDataFrame(
    [Row(name="Alice", age=25), Row(name="Bob", age=30)]
)

def process_row(row):
    print(f"Processing: {row.name} - Age {row.age}")

df.foreach(process_row)
```

---

## 📌 Example 4: Writing DataFrame Rows to a Database

```python
def save_to_db(row):
    # Example: pseudo code for DB insert
    query = f"INSERT INTO users (name, age) VALUES ('{row.name}', {row.age})"
    print(query)  # Replace with DB execution

df.foreach(save_to_db)
```

---

## 🚀 When to Use

* Writing each row to an external system (DB, file, API).
* Logging for debugging purposes.
* Running custom processing on each element **without returning a new dataset**.

---

## 🛑 When NOT to Use

* Avoid heavy computation inside `foreach()` because it runs on worker nodes and can slow down the job.
* Do not use it when you need to transform data and reuse it — use `map()` or DataFrame operations instead.

---

