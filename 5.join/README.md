# 📌 PySpark — Joins

---

## 🔹 Overview
In PySpark, **joins** are used to combine rows from two DataFrames based on matching column values.  
The method **`DataFrame.join()`** supports multiple join types, similar to SQL.

---

## 🔹 Syntax
```python
DataFrame.join(
    other,                # DataFrame to join with
    on=None,               # Column(s) to join on
    how=None               # Type of join (string)
)
````

| Parameter | Description                                                                                     |
| --------- | ----------------------------------------------------------------------------------------------- |
| **other** | DataFrame to join with.                                                                         |
| **on**    | Column name(s) to join on (string or list).                                                     |
| **how**   | Join type (`'inner'`, `'outer'`, `'left'`, `'right'`, `'left_semi'`, `'left_anti'`, `'cross'`). |

---

## 🔹 Types of Joins

| Join Type                    | Description                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------ |
| **inner**                    | Returns matching rows from both DataFrames.                                          |
| **outer** / **full**         | Returns all rows from both DataFrames, with nulls where no match.                    |
| **left** / **left\_outer**   | All rows from left DataFrame + matching rows from right.                             |
| **right** / **right\_outer** | All rows from right DataFrame + matching rows from left.                             |
| **left\_semi**               | Returns only left DataFrame rows that have a match in the right DataFrame.           |
| **left\_anti**               | Returns only left DataFrame rows that **don’t** have a match in the right DataFrame. |
| **cross**                    | Cartesian product of rows.                                                           |

---

## 🔹 Example Dataset

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("JoinExample").getOrCreate()

data1 = [(1, "Alice"), (2, "Bob"), (3, "Charlie")]
data2 = [(1, "HR"), (2, "IT"), (4, "Finance")]

df1 = spark.createDataFrame(data1, ["id", "name"])
df2 = spark.createDataFrame(data2, ["id", "dept"])
```

---

## 🔹 Example 1 — Inner Join

```python
inner_df = df1.join(df2, on="id", how="inner")
inner_df.show()
```

**Output**

```
+---+-----+---+
| id| name|dept|
+---+-----+----+
|  1|Alice|  HR|
|  2|  Bob|  IT|
+---+-----+----+
```

---

## 🔹 Example 2 — Left Join

```python
left_df = df1.join(df2, on="id", how="left")
left_df.show()
```

**Output**

```
+---+-------+------+
| id|   name|  dept|
+---+-------+------+
|  1|  Alice|    HR|
|  2|    Bob|    IT|
|  3|Charlie|  null|
+---+-------+------+
```

---

## 🔹 Example 3 — Right Join

```python
right_df = df1.join(df2, on="id", how="right")
right_df.show()
```

**Output**

```
+---+-------+-------+
| id|   name|   dept|
+---+-------+-------+
|  1|  Alice|     HR|
|  2|    Bob|     IT|
|  4|   null|Finance|
+---+-------+-------+
```

---

## 🔹 Example 4 — Full Outer Join

```python
outer_df = df1.join(df2, on="id", how="outer")
outer_df.show()
```

**Output**

```
+---+-------+-------+
| id|   name|   dept|
+---+-------+-------+
|  1|  Alice|     HR|
|  2|    Bob|     IT|
|  3|Charlie|   null|
|  4|   null|Finance|
+---+-------+-------+
```

---

## 🔹 Example 5 — Left Semi Join

```python
semi_df = df1.join(df2, on="id", how="left_semi")
semi_df.show()
```

**Output**

```
+---+-----+
| id| name|
+---+-----+
|  1|Alice|
|  2|  Bob|
+---+-----+
```

---

## 🔹 Example 6 — Left Anti Join

```python
anti_df = df1.join(df2, on="id", how="left_anti")
anti_df.show()
```

**Output**

```
+---+-------+
| id|   name|
+---+-------+
|  3|Charlie|
+---+-------+
```

---

## 🔹 Example 7 — Cross Join

```python
cross_df = df1.crossJoin(df2)
cross_df.show()
```

**Output** (Cartesian product)

```
+---+-------+---+-------+
| id|   name| id|   dept|
+---+-------+---+-------+
|  1|  Alice|  1|     HR|
|  1|  Alice|  2|     IT|
|  1|  Alice|  4|Finance|
|  2|    Bob|  1|     HR|
|  2|    Bob|  2|     IT|
|  2|    Bob|  4|Finance|
|  3|Charlie|  1|     HR|
| ... rows omitted ...
```

---

## 🔹 Notes & Best Practices

1. For **multiple join keys**, pass a list:

   ```python
   df1.join(df2, on=["id", "dept"], how="inner")
   ```
2. If column names differ, use:

   ```python
   df1.join(df2, df1.id == df2.emp_id, "inner")
   ```
3. Always filter unnecessary columns after join to avoid large DataFrames.
4. Cross joins can be **very large** — use with caution.

---

✅ **Summary:**
PySpark supports multiple join types similar to SQL, with flexible options for matching keys, handling nulls, and combining datasets.

