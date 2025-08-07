# 🔁 PySpark: `distinct()` and `dropDuplicates()`

Both `distinct()` and `dropDuplicates()` are used to **remove duplicate rows** in a PySpark DataFrame, but they have important differences in behavior and usage.

---

## 🧱 Sample DataFrame

```python
data = [
    ("Alice", "Sales", 1000),
    ("Alice", "Sales", 1000),
    ("Bob", "HR", 1200),
    ("Bob", "Finance", 1200),
    ("Charlie", "HR", 1300)
]
columns = ["name", "dept", "salary"]
df = spark.createDataFrame(data, columns)
df.show()
````

---

## ✅ 1. `distinct()` – Removes **entire duplicate rows**

```python
df.distinct().show()
```

### 🔍 Behavior:

* Removes rows where **all column values** are the same.
* Equivalent to `SELECT DISTINCT *` in SQL.

---

## ✅ 2. `dropDuplicates()` – Remove duplicates based on **specific columns**

```python
df.dropDuplicates(["name"]).show()
df.dropDuplicates(["dept", "salary"]).show()
```

### 🔍 Behavior:

* Keeps **first occurrence** of a duplicate based on given subset of columns.
* Allows **column-based deduplication**.

---

## 📊 Comparison Table

| Feature                | `distinct()`               | `dropDuplicates(cols)`              |
| ---------------------- | -------------------------- | ----------------------------------- |
| Scope                  | All columns                | Subset of columns                   |
| Use-case               | Remove full row duplicates | Remove based on selected column(s)  |
| SQL equivalent         | `SELECT DISTINCT *`        | `SELECT * FROM table GROUP BY cols` |
| Custom columns allowed | ❌ No                       | ✅ Yes                               |

---

## 🧪 Example Output

### Original DataFrame

```
+-------+--------+------+
|  name |   dept |salary|
+-------+--------+------+
| Alice |  Sales |  1000|
| Alice |  Sales |  1000|
|   Bob |     HR |  1200|
|   Bob |Finance |  1200|
|Charlie|     HR |  1300|
+-------+--------+------+
```

### df.distinct()

```
+-------+--------+------+
|  name |   dept |salary|
+-------+--------+------+
| Alice |  Sales |  1000|
|   Bob |Finance |  1200|
|   Bob |     HR |  1200|
|Charlie|     HR |  1300|
+-------+--------+------+
```

### df.dropDuplicates(\["name"])

```
+-------+--------+------+
|  name |   dept |salary|
+-------+--------+------+
| Alice |  Sales |  1000|
|   Bob |     HR |  1200|
|Charlie|     HR |  1300|
+-------+--------+------+
```

---

✅ **Best Practice**:
Use `dropDuplicates(["col1", "col2", ...])` when you want to control which duplicates are removed based on **business logic**.

