# 🧼 PySpark: `fillna()` vs `fill()`

Both `fillna()` and `fill()` are used to **replace NULL or missing values** in a PySpark DataFrame. `fill()` is just an alias for `fillna()`.

---

## 🧱 Sample DataFrame

```python
data = [
    ("James", None, "M"),
    ("Ann", "NY", None),
    ("Tom", None, None)
]
columns = ["name", "city", "gender"]
df = spark.createDataFrame(data, columns)
df.show()
````

---

## ✅ 1. `fillna()` – Replace `NULL` values

```python
# Fill all NULLs with same value
df.fillna("Unknown").show()

# Fill NULLs by specific column
df.fillna({"city": "NoCity", "gender": "NoGender"}).show()
```

---

## ✅ 2. `fill()` – Exact same as `fillna()` (alias method)

```python
df.fill({"city": "NA", "gender": "NA"}).show()
```

---

## 🧪 Output Example

### Original DataFrame:

```
+-----+----+------+
| name|city|gender|
+-----+----+------+
|James|null|     M|
|  Ann|  NY|  null|
|  Tom|null|  null|
+-----+----+------+
```

### df.fillna("Unknown")

```
+-----+--------+--------+
| name|    city|  gender|
+-----+--------+--------+
|James| Unknown|       M|
|  Ann|      NY| Unknown|
|  Tom| Unknown| Unknown|
+-----+--------+--------+
```

### df.fillna({"city": "NoCity", "gender": "NoGender"})

```
+-----+--------+---------+
| name|    city|   gender|
+-----+--------+---------+
|James| NoCity|        M|
|  Ann|     NY| NoGender|
|  Tom| NoCity| NoGender|
+-----+--------+---------+
```

---

## 📊 Comparison Table

| Feature               | `fillna()`                 | `fill()`                   |
| --------------------- | -------------------------- | -------------------------- |
| Purpose               | Fill NULLs                 | Fill NULLs (alias)         |
| Fill all columns      | ✅                          | ✅                          |
| Fill specific columns | ✅ with dict `{col: value}` | ✅ with dict `{col: value}` |
| Numeric-only support  | ✅ with int/float           | ✅ with int/float           |
| Alias method          | Main method                | Alias of `fillna()`        |

---

## 📝 Best Practice

* Use `fillna()` explicitly for clarity.
* Always prefer dictionary format `{col: value}` when filling specific columns.

