# 🔄 PySpark **Pivot** and **Unpivot**

In PySpark, **Pivot** and **Unpivot** are used to reshape data —  
**Pivot** transforms *rows → columns*, while **Unpivot** transforms *columns → rows*.

---

## 📌 1. Pivot

### 🛠 Syntax
```python
DataFrame.groupBy(grouping_columns).pivot(pivot_column, [values]).agg(aggregation)
````

| Parameter          | Description                                                                   |
| ------------------ | ----------------------------------------------------------------------------- |
| `grouping_columns` | Column(s) to group the data before pivoting                                   |
| `pivot_column`     | Column whose unique values will become new columns                            |
| `values`           | Optional list of values to pivot (if omitted, Spark determines automatically) |
| `aggregation`      | Aggregation function to apply to values                                       |

---

### 📍 Example: Pivot in PySpark

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder.appName("PivotExample").getOrCreate()

data = [
    ("John", "Math", 80),
    ("John", "Science", 90),
    ("Mike", "Math", 70),
    ("Mike", "Science", 85)
]
df = spark.createDataFrame(data, ["name", "subject", "score"])

pivot_df = df.groupBy("name").pivot("subject").agg(sum("score"))
pivot_df.show()
```

**Output:**

```
+----+----+-------+
|name|Math|Science|
+----+----+-------+
|Mike|  70|     85|
|John|  80|     90|
+----+----+-------+
```

---

## 📌 2. Unpivot (Melt)

PySpark doesn’t have a direct **`unpivot()`** function like Pandas,
but we can achieve it using `selectExpr` and `stack()`.

---

### 🛠 Syntax

```python
df.selectExpr(id_columns..., "stack(N, col1, 'name1', col2, 'name2', ...) as (col_name, value)")
```

| Parameter                      | Description                                         |
| ------------------------------ | --------------------------------------------------- |
| `N`                            | Number of columns to unpivot                        |
| `col1, 'name1', col2, 'name2'` | Column name and corresponding label for melted rows |
| `(col_name, value)`            | New column names for the melted result              |

---

### 📍 Example: Unpivot in PySpark

```python
unpivot_df = pivot_df.selectExpr(
    "name",
    "stack(2, Math, 'Math', Science, 'Science') as (subject, score)"
)
unpivot_df.show()
```

**Output:**

```
+----+-------+-----+
|name|subject|score|
+----+-------+-----+
|Mike|   Math|   70|
|Mike|Science|   85|
|John|   Math|   80|
|John|Science|   90|
+----+-------+-----+
```

---

## 📊 Summary Table

| Operation   | Purpose        | Key Function                  | Result Shape |
| ----------- | -------------- | ----------------------------- | ------------ |
| **Pivot**   | Rows → Columns | `pivot()` with `groupBy()`    | Wider        |
| **Unpivot** | Columns → Rows | `stack()` with `selectExpr()` | Longer       |

---

## ⚡ Performance Tips

* For **pivot**, always pre-filter data to reduce unnecessary columns.
* Avoid pivoting on **high-cardinality columns** (can cause huge DataFrames).
* For **unpivot**, stack function requires you to **manually specify** all columns.

---