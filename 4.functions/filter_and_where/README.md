# 🔍 PySpark: `filter()` vs `where()`

In PySpark, `filter()` and `where()` are used to **filter rows from a DataFrame** based on a condition.  
Both methods are **identical** in functionality and interchangeable.

---

### 🧱 Sample DataFrame

```python
data = [
    ("James", "Sales", 3000),
    ("Michael", "HR", 4000),
    ("Robert", "IT", 2500),
    ("Maria", "IT", 3000)
]
columns = ["name", "dept", "salary"]
df = spark.createDataFrame(data, columns)
df.show()
````

---

### ✅ 1. `filter()` – Filter rows using condition

```python
# Salary > 3000
df.filter(df.salary > 3000).show()

# Multiple conditions
df.filter((df.dept == "IT") & (df.salary >= 3000)).show()
```

---

### ✅ 2. `where()` – Same as `filter()`, SQL-style alias

```python
# Same condition using where()
df.where(df.salary > 3000).show()

# With multiple conditions
df.where((df.dept == "IT") & (df.salary >= 3000)).show()
```

---

### ✅ 3. Using SQL expression (both methods support this)

```python
# Using SQL expression string
df.filter("salary > 3000 AND dept = 'HR'").show()
df.where("salary > 3000 AND dept = 'HR'").show()
```

---

### 🧪 Output Example

### Original DataFrame:

```
+--------+-------+------+
|    name|   dept|salary|
+--------+-------+------+
|   James|  Sales|  3000|
| Michael|     HR|  4000|
|  Robert|     IT|  2500|
|   Maria|     IT|  3000|
+--------+-------+------+
```

### Filtered (salary > 3000):

```
+--------+-----+------+
|    name|dept |salary|
+--------+-----+------+
| Michael| HR  |  4000|
+--------+-----+------+
```

---

### 📊 Comparison Table

| Feature                | `filter()`     | `where()`                     |
| ---------------------- | -------------- | ----------------------------- |
| Functionality          | Filter rows    | Same as `filter()`            |
| SQL expression support | ✅              | ✅                             |
| Alias of               | Primary method | Alias of `filter()`           |
| Preferred for SQL feel | ❌              | ✅ (for SQL-style readability) |

---

### ✅ Best Practice

* Use `filter()` in general for clarity in API.
* Use `where()` if you're writing SQL-like expressions or for better readability in mixed syntax scenarios.

> ℹ️ They **compile to the same execution plan** internally.

---
## 🔎 PySpark Filter Examples: Different Ways to Filter Data

Below are various examples of how you can use `filter()` / `where()` in PySpark to extract subsets of your data.

---

### 🧱 Sample DataFrame

```python
data = [
    ("James", "Sales", 3000),
    ("Michael", "HR", 4000),
    ("Robert", "IT", 2500),
    ("Maria", "IT", 3000),
    ("Jen", "Finance", 3900),
    ("Jeff", None, None)
]
columns = ["name", "dept", "salary"]
df = spark.createDataFrame(data, columns)
df.show()
````

---

### ✅ 1. Filter rows by numeric value

```python
df.filter(df.salary > 3000).show()
```

---

### ✅ 2. Filter rows by string value

```python
df.filter(df.dept == "IT").show()
```

---

### ✅ 3. Filter with multiple conditions (AND, OR)

```python
from pyspark.sql.functions import col

# AND condition
df.filter((df.dept == "IT") & (df.salary >= 3000)).show()

# OR condition
df.filter((df.dept == "IT") | (df.salary >= 4000)).show()
```

---

### ✅ 4. Filter using SQL expression string

```python
df.filter("dept = 'HR' AND salary > 3000").show()
```

---

### ✅ 5. Filter rows with NULL and NOT NULL

```python
df.filter(df.salary.isNull()).show()
df.filter(df.salary.isNotNull()).show()
```

---

### ✅ 6. Filter rows with `isin()` (like SQL IN)

```python
df.filter(df.dept.isin("IT", "Finance")).show()
```

---

### ✅ 7. Filter using `like()` (wildcard matching)

```python
df.filter(df.name.like("J%")).show()  # names starting with J
```

---

### ✅ 8. Filter using `startswith()` and `endswith()`

```python
df.filter(df.name.startswith("M")).show()
df.filter(df.name.endswith("a")).show()
```

---

### ✅ 9. Filter using `between()`

```python
df.filter(df.salary.between(2500, 3500)).show()
```

---

### ✅ 10. Negation using `~` (NOT condition)

```python
df.filter(~df.dept.isin("HR", "Finance")).show()
```

---

### 📝 Best Practice

* Use **column expressions** (`col("salary") > 3000`) for flexibility.
* Combine with `select()` to limit columns returned.
* SQL expression strings are good for quick filters but less safe than column APIs (prone to typos and less IDE-friendly).


